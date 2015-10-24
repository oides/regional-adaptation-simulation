"""
Represents each node on distributed environment in charge of execute jobs.

"""
__author__ = 'Eudes Santos Andrade'


from report import Report
from controlfunctions import ControlFunctions
from environment import SimulationEnvironment
from region import Region
import simconfig


class Controller(object):

    def __init__(self, simpyEnvironment):
        self.time = 0
        self.simpyEnvironment = simpyEnvironment
    
    def startOperation(self):
        while True:
            yield self.simpyEnvironment.timeout(self.tunning())
            
    def tunning(self):
            # Report.addJobsExecutedOnNodes(self.identificador)
            # return ControlFunctions.calculate_job_cost(self.simulationEnvironment.NIVEL_ATUAL_PERT, self.region.region_size)
            print('Tunando')
            return simconfig.CONTROLLER_FREQUENCY
