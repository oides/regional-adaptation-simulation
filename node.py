"""
Represents each node on distributed environment in charge of execute jobs.

"""
__author__ = 'Eudes Santos Andrade'


from report import Report
from controlfunctions import ControlFunctions
from environment import SimulationEnvironment
from region import Region


class Node(object):

    def __init__(self, simpyEnvironment, simulationEnvironment, region, identificador):
        self.identificador = identificador
        self.simulationEnvironment = simulationEnvironment    # Mantem localmente informações do ambiente sob o qual o nó está inserido
        self.simpyEnvironment = simpyEnvironment    # Mantem localmente informações do ambiente sob o qual o nó está inserido
        self.region = region    # Hold the current region configuration

    def iniciarOperacao(self):
        while True:
            yield self.simpyEnvironment.timeout(self.executarTrabalho())
            
    def executarTrabalho(self):
            Report.addJobsExecutedOnNodes(self.identificador)
            return ControlFunctions.calculate_job_cost(self.simulationEnvironment.NIVEL_ATUAL_PERT, self.region.region_size)
            
