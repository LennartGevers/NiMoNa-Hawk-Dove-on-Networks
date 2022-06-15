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



    def run(self, timesteps, n_migrate=1):
        #Durchfuehrung der Simulation
        #Fuehrt die Entwicklung des Modells an dem uebergebenen Netzwerk mit den
        #uebergebenen Replikator- und Migrationsfunktionen durch
        #
        #@param     {Integer}   timesteps       Zahl der Entwicklungsschrittet
        #@param     {Integer}   [n_migrate]     Zahl der Anwendungen der Migrationsdynamik pro Entwicklungsschritt    


        self.network_history = [None] * len(self.environment)


        for t in range(0, timesteps):

            #Entwicklung des neuen Zustandes
            replicator_dynamics(self.environment, t, self.reward, self.harm)

            #Mehrfache Anwendung der Migrationsfunktion um Diskretisierungsfehler vorzubeugen
            for _ in range(0, n_migrate):
                self.migrate(self.environment)

            self._save_environment()

        return self.network_history