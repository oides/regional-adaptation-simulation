"""
Represents each node on distributed environment in charge of execute jobs.

"""
__author__ = 'Eudes Santos Andrade'


from report import Report
from controlfunctions import ControlFunctions
from environment import SimulationEnvironment
from region import Region
import simconfig
import copy


class Controller(object):

    def __init__(self, simpyEnvironment, simulationEnvironment):
        self.time = 0
        self.simpyEnvironment = simpyEnvironment
        self.simulationEnvironment = simulationEnvironment
        self.lastCountJobsExecutedOnNodes = None
    
    def startOperation(self):
        while True:
            yield self.simpyEnvironment.timeout(self.tunning())
            
    def tunning(self):
        # Report.addJobsExecutedOnNodes(self.identificador)
        # return ControlFunctions.calculate_job_cost(self.simulationEnvironment.NIVEL_ATUAL_PERT, self.region.region_size)

        jobsExecutedOnNodes = {node.identificador: node.jobsExecuted for node in self.simulationEnvironment.nodes}
        controlledVariable = 0
        
        if self.lastCountJobsExecutedOnNodes is not None:            
            for nodeId in self.lastCountJobsExecutedOnNodes:
                lastCount = self.lastCountJobsExecutedOnNodes[nodeId]
                currentCount = jobsExecutedOnNodes[nodeId]
                
                controlledVariable += (currentCount - lastCount)
                
            controlledVariable /= len(self.lastCountJobsExecutedOnNodes)
        
            actuation_value = ControlFunctions.calculate_actuation_value(controlledVariable)
                
            self.simulationEnvironment.region.region_size += actuation_value                
                
            print('Controlled Variable: ' + str(controlledVariable))
            print('Actuation Value: ' + str(actuation_value))
                
        self.lastCountJobsExecutedOnNodes = jobsExecutedOnNodes
        
        return simconfig.CONTROLLER_FREQUENCY
