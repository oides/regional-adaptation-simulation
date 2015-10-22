"""
Represents each node on distributed environment in charge of execute jobs.

"""
__author__ = 'Eudes Santos Andrade'


from report import Report


class Node(object):

    def __init__(self, simulationEnvironment, simpyEnvironment, identificador):
        self.identificador = identificador
        self.simulationEnvironment = simulationEnvironment    # Mantem localmente informações do ambiente sob o qual o nó está inserido
        self.simpyEnvironment = simpyEnvironment    # Mantem localmente informações do ambiente sob o qual o nó está inserido

    def iniciarOperacao(self):
        while True:
            yield self.simpyEnvironment.timeout(self.executarTrabalho())
            
    def executarTrabalho(self):
            Report.addJobsExecutedOnNodes(self.identificador)
            return self.simulationEnvironment.NIVEL_ATUAL_PERT
            
