import numpy as np
import matplotlib.pyplot as plt

from src.model.replicator_dynamics.replicator_dynamics import replicator_dynamics

class simulation:

    def __init__(self, environment, reward_function, harm_function, migration_function):
        self.environment = environment              #
        self.reward = reward_function               #
        self.harm = harm_function                   #
        self.migrate = migration_function           #

        self.network_history = []                   #Liste der Entwicklungen aller Nodes, wobei diese jeweils Listen mit den Vektoren der Nodes zu jedem Zeitschritt sind



    def _save_environment(self):
        #Interne Funktion zur Speicherung eines Netzwerkzustandes in der network_history Liste
        for i in range(0, len(self.environment)):

            self.network_history[i].append(self.environment[i].getValue())



    def run(self, timesteps, background_fitness=0, n_migrate=1):
        #Durchfuehrung der Simulation
        #Fuehrt die Entwicklung des Modells an dem uebergebenen Netzwerk mit den
        #uebergebenen Replikator- und Migrationsfunktionen durch
        #
        #@param     {Integer}   timesteps       Zahl der Entwicklungsschrittet
        #@param     {Integer}   [n_migrate]     Zahl der Anwendungen der Migrationsdynamik pro Entwicklungsschritt    


        self.network_history = [None] * len(self.environment)


        for t in range(0, timesteps):

            #Entwicklung des neuen Zustandes
            replicator_dynamics(self.environment, t, self.reward, self.harm, b=background_fitness)

            #Mehrfache Anwendung der Migrationsfunktion um Diskretisierungsfehler vorzubeugen
            for _ in range(0, n_migrate):
                self.migrate(self.environment)

            self._save_environment()

        return self.network_history


    def plot(self, plot_sum=True):
        #Erstellt einen Plot einer durchgefuehrten Simulation
        #Plottet die zeitliche Entwicklung der Werte der Netzwerkknoten

        #@param {boolean} sum           Die Summe als Hawk bzw. Doves wird zusätzlich geplottet wenn dieser Parameter auf true steht

        #Methode wird nur ausgefueht wenn network_history keine Leere Liste ist, also run() seit initialisierung bereits durchgefuehrt wurde
        if(len(self.network_history)):
            t = np.arange(0, len(self.network_history[0]))

            #Plot der Entwicklungen der einzelnen Nodes
            for hawk_i, dove_i in self.network_history:
                plt.plot(t, hawk_i)
                plt.plot(t, dove_i)

            #Plot der Gesamtentwicklung des Netzwerks
            if(plot_sum):

                sum_hawks = sum( [ np.array(hawk_i) for hawk_i, dove_i in self.network_history])
                sum_doves = sum( [ np.array(dove_i) for hawk_i, dove_i in self.network_history])

                plt.plot(t, sum_hawks)
                plt.plot(t, sum_doves)
                    
        else:
            raise RuntimeError('Die Simulation wurde noch nicht durchgelaufen.')