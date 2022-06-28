import numpy as np
import matplotlib.pyplot as plt
import time

from src.model.replicator_dynamics.replicator_dynamics import replicator_dynamics

class simulation:

    def __init__(self, environment, reward_function, harm_function, migration_function):
        self.environment = environment              #Liste der Netzwerk-Knoten
        self.reward = reward_function               #Reward-Funktion mit Signatur reward(int t, float tuple (Werte des Nodes), position tuple)
        self.harm = harm_function                   #Harm-Funktion mit Signatur reward(int t, float tuple (Werte des Nodes), position tuple)
        self.migrate = migration_function           #Migrationsfunktion mit Signatur migration_function(list nodes)

        self.network_history = []                   #Liste der Entwicklungen aller Nodes, wobei diese jeweils Listen mit den Vektoren der Nodes zu jedem Zeitschritt sind


    def _save_environment(self):
        #Interne Funktion zur Speicherung eines Netzwerkzustandes in der network_history Liste
        for i in range(0, len(self.environment)):

            hawk_i, dove_i = self.environment[i].get_value()
            self.network_history[i][0].append(hawk_i)
            self.network_history[i][1].append(dove_i)

    def _setup_history(self):
        #Vorbereitung der network_history Liste
        self.network_history = []
        for i in range(0, len(self.environment)):
            self.network_history.append([])
            self.network_history[i].append([])
            self.network_history[i].append([])

    def run(self, timesteps, background_fitness=0, n_migrate=1, n_replicate=1):
        #Durchfuehrung der Simulation
        #Fuehrt die Entwicklung des Modells an dem uebergebenen Netzwerk mit den
        #uebergebenen Replikator- und Migrationsfunktionen durch
        #
        #@param     {Integer}   timesteps       Zahl der Entwicklungsschrittet
        #@param     {Integer}   [n_migrate]     Zahl der Anwendungen der Migrationsdynamik pro Entwicklungsschritt    


        self._setup_history()

        for t in range(0, timesteps):

            #Entwicklung des neuen Zustandes
            for _ in range(0, n_replicate):
                replicator_dynamics(self.environment, t, self.reward, self.harm, b=background_fitness)

            #Mehrfache Anwendung der Migrationsfunktion um Diskretisierungsfehler vorzubeugen
            for _ in range(0, n_migrate):
                self.migrate(self.environment, t)

            self._save_environment()

        return self.environment


    def plot_graph(self, plot_sum=True):
        #Erstellt einen Plot einer durchgefuehrten Simulation
        #Plottet die zeitliche Entwicklung der Werte der Netzwerkknoten

        #@param {boolean} sum           Die Summe als Hawk bzw. Doves wird zusätzlich geplottet wenn dieser Parameter auf true steht

        #Methode wird nur ausgefuehrt wenn network_history keine Leere Liste ist, also run() seit initialisierung bereits durchgefuehrt wurde
        if(len(self.network_history)):
            t = np.arange(0, len(self.network_history[0][0]))

            #Plot der Entwicklungen der einzelnen Nodes
            for hawk_i, dove_i in self.network_history:
                plt.plot(t, hawk_i, color='orange')
                plt.plot(t, dove_i, color='navy')

            #Plot der Gesamtentwicklung des Netzwerks (Summen aller Netzwerke)
            if(plot_sum):

                sum_hawks = sum( [ np.array(hawk_i) for hawk_i, dove_i in self.network_history])
                sum_doves = sum( [ np.array(dove_i) for hawk_i, dove_i in self.network_history])

                plt.plot(t, sum_hawks, color='orange', label='Summe Hawks')
                plt.plot(t, sum_doves, color='navy', label='Summe Doves')
                plt.plot(t, np.array(sum_hawks) + np.array(sum_doves), color='black')
                    
        else:
            raise RuntimeError('Die Simulation wurde noch nicht durchgelaufen.')

    def draw_node_animatable(self, ax, node, max_markersize):
        x, y = node.get_position()
        val = node.get_value()[0] + node.get_value()[1]

        hawk_share = node.get_value()[0] / (val)

        marker, = ax.plot(x,y, marker='.', markersize=max_markersize*(abs(np.sqrt(val)))+2, color=str(0.6*hawk_share))
        return marker

    def draw_connection(self, ax, node_1, node_2):
        x1, y1 = node_1.get_position()
        x2, y2 = node_2.get_position()

        ax.plot([x1, x2], [y1, y2], marker='', color='black', linewidth=0.1)

    def plot_network(self, max_markersize=8):
        t_interval = np.arange(0, len(self.network_history[0][0]))
        
        # to run GUI event loop
        plt.ion()

        figure, ax = plt.subplots()

        markers = []

        #Creating initial Network
        for node in self.environment:

            for connection in node.get_connections():
                self.draw_connection(ax, node, connection[0])

            markers.append(self.draw_node_animatable(ax, node, max_markersize*len(self.environment)))


        for t in t_interval:
            for i in range(0, len(self.network_history)):

                val = self.network_history[i][0][t] + self.network_history[i][1][t]

                hawk_share = self.network_history[i][0][t] / (val)

                markers[i].set_markersize(max_markersize*len(self.environment)*(abs(np.sqrt(val)))+2)
                markers[i].set_color(str(0.6*hawk_share))
            
            figure.canvas.draw()
            figure.canvas.flush_events()
            
            time.sleep(0.02)