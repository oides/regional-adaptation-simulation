"""
Implements the simulation environment meta-information.

"""
__author__ = 'Eudes Santos Andrade'


import random
import simconfig
from report import Report


class SimulationEnvironment(object):
    
    def __init__(self, simpyEnvironment):

        self.simpyEnvironment = simpyEnvironment    # Hold the simpy environment
        self.nodes = None   # Each node on distributed environment in charge of execute jobs
        self.region = None  # Region defined on regional planner pattern
        self.jobs = 0  # Jobs List wating for execution
        self.idleLoops = 0  # Jobs List wating for execution

        self.NIVEL_ATUAL_PERT = simconfig.BASE_DISTURBING_LEVEL # Define o nível da perturbação inserida no ambiente
        
    def start_disturbing(self):
    
        while True:
            yield self.simpyEnvironment.timeout(self.generate_disturbing())

    def start_jobs(self):

        while True:
            yield self.simpyEnvironment.timeout(self.generate_jobs())
            self.jobs += 1

    def generate_disturbing(self):

        self.NIVEL_ATUAL_PERT = random.randint(simconfig.BASE_DISTURBING_LEVEL-simconfig.INTERVAL_DISTURBING_LEVEL, simconfig.BASE_DISTURBING_LEVEL+simconfig.INTERVAL_DISTURBING_LEVEL)
        intervaloProximaPerturbacao = random.randint(simconfig.BASE_DISTURBING_PERIOD - simconfig.INTERVAL_DISTURBING_PERIOD, simconfig.BASE_DISTURBING_PERIOD + simconfig.INTERVAL_DISTURBING_PERIOD)
        
        Report.add_disturbing(str(self.NIVEL_ATUAL_PERT), str(intervaloProximaPerturbacao), self.simpyEnvironment.now)
        
        return intervaloProximaPerturbacao

    def generate_jobs(self):

        return simconfig.JOBS_FREQUENCY # Define a frequencia com que os jobs chegam na fila
