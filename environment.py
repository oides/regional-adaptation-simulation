"""
Implements the simulation environment meta-information.

"""
__author__ = 'Eudes Santos Andrade'


import random
from report import Report


class SimulationEnvironment(object):
    
    def __init__(self, simpyEnvironment):

        self.simpyEnvironment = simpyEnvironment    # Hold the simpy environment
        self.T_INTER_PERT = 5    # Cria uma nova perturbacão a cada 4 minutos
        self.T_VAR_INTER_PERT = 3  # Intervalo de variação do instante de criação de nova perturbação
        self.NIVEL_BASE_PERT = 5 # Define o nível da perturbação inserida no ambiente
        self.VAR_NIVEL_BASE_PERT = 4 # Define o nível da perturbação inserida no ambiente
        self.NIVEL_ATUAL_PERT = self.NIVEL_BASE_PERT # Define o nível da perturbação inserida no ambiente

    def startDisturbing(self):
    
        while True:
            yield self.simpyEnvironment.timeout(self.generateDisturbing())

    def generateDisturbing(self):
        
        self.NIVEL_ATUAL_PERT = random.randint(self.NIVEL_BASE_PERT-self.VAR_NIVEL_BASE_PERT, self.NIVEL_BASE_PERT+self.VAR_NIVEL_BASE_PERT)
        intervaloProximaPerturbacao = random.randint(self.T_INTER_PERT-self.T_VAR_INTER_PERT, self.T_INTER_PERT+self.T_VAR_INTER_PERT)
        
        Report.addDisturbing(str(self.NIVEL_ATUAL_PERT), str(intervaloProximaPerturbacao), self.simpyEnvironment.now)
        
        return intervaloProximaPerturbacao
