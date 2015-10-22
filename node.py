"""
Represents each node on distributed environment in charge of execute jobs.

"""
__author__ = 'Eudes Santos Andrade'


class Node(object):

    def __init__(self, environment, simpyEnvironment, identificador):
        self.identificador = identificador
        self.environment = environment    # Mantem localmente informações do ambiente sob o qual o nó está inserido
        self.simpyEnvironment = simpyEnvironment    # Mantem localmente informações do ambiente sob o qual o nó está inserido
        self.numeroJobsExecutados = 0

    def iniciarOperacao(self):
        while True:
            yield self.simpyEnvironment.timeout(self.executarTrabalho())
            
    def executarTrabalho(self):
            self.numeroJobsExecutados += 1
            return self.environment.NIVEL_ATUAL_PERT
            
