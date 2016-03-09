"""
Represents each node on distributed environment in charge of execute jobs.

"""
__author__ = 'Eudes Santos Andrade'


from report import Report
from controlfunctions import ControlFunctions
from environment import SimulationEnvironment
from region import Region


class Node(object):

    def __init__(self, simpyEnvironment, simulationEnvironment, identificador):
        self.identificador = identificador
        self.simulationEnvironment = simulationEnvironment    # Mantem localmente informações do ambiente sob o qual o nó está inserido
        self.simpyEnvironment = simpyEnvironment    # Mantem localmente informações do ambiente sob o qual o nó está inserido
        self.jobsExecuted = 0    # Counter to executed jobs on node

    def iniciarOperacao(self):
        while True:
            yield self.simpyEnvironment.timeout(self.executarTrabalho())
            
    def executarTrabalho(self):

        if self.simulationEnvironment.jobs > 0:
            self.simulationEnvironment.jobs -= 1
            self.jobsExecuted += 1
            Report.add_jobs_executed_on_nodes(self.identificador)

            return ControlFunctions.calculate_job_cost(self.simulationEnvironment.NIVEL_ATUAL_PERT, self.simulationEnvironment.region._region_size)
        else:
            self.simulationEnvironment.idleLoops += 1
            Report.add_idle_cycle()
            return 1