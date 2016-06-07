"""
Simulação para avaliação do tradeoff existente entre overhead introduzido e a economia
de recursos computacionais após adoção de um planejamento regional adaptativo.

Objeto de adaptação: tamanho das regiões.

"""
__author__ = 'Eudes Santos Andrade'


import random

import sys
import simpy
import simconfig
from environment import SimulationEnvironment
from controlfunctions import ControlFunctions
from node import Node
from report import Report
from region import Region
from controller import Controller


def addDisturbing():
    simpyEnvironment.process(simulationEnvironment.start_disturbing())
        
        
def addJobs():
    simpyEnvironment.process(simulationEnvironment.start_jobs())


def addNodes(amount):
    nodes = []
    
    for x in range(amount):
        newNode = Node(simpyEnvironment, simulationEnvironment, 'Node ' + str(x))
        nodes.append(newNode)
        simpyEnvironment.process(newNode.iniciarOperacao()) # Processo que adiciona novo no ambiente da simulação
    
    simulationEnvironment.nodes = nodes
    
    return nodes


def addController(controllerEnabled):
    print('Controller ' + controllerEnabled + '...')
    if controllerEnabled == 'enabled':
        controller = Controller(simpyEnvironment, simulationEnvironment, 0.2, 0.2, 0.2)
        controller.setPoint(simconfig.SET_POINT)
        simpyEnvironment.process(controller.startOperation()) # Processo que adiciona novo no ambiente da simulação
        

def addRegion():
    region = Region(simpyEnvironment)
    simulationEnvironment.region = region

REPLICATIONS = sys.argv[1]

# Configuração e início da Simulação
print('Starting simulation [replication ' + REPLICATIONS + '][seed ' + sys.argv[2] + ']...')

# Semente para reprodução de resultados
if simconfig.ENABLE_SEED:
    print('Usando semente: ' + simconfig.RANDOM_SEED)
    random.seed(simconfig.RANDOM_SEED)

# Criando o environment do simpy
simpyEnvironment = simpy.Environment()

# Building the simulation environment
simulationEnvironment = SimulationEnvironment(simpyEnvironment)

# Building the simulation region configuration
addRegion()

# Adding disturbing process
addDisturbing() # Processo que adiciona perturbação ao ambiente da simulação

# Adding Jobs
addJobs() # Processo que adiciona jobs ao ambiente da simulação

# Adding node
addNodes(simconfig.NODES_NUMBER)

# Building the distributed system controller
addController(sys.argv[3])

# Configuring enviroment on control functions
ControlFunctions.simpyEnvironment = simpyEnvironment

# Executando a simulação
simpyEnvironment.run(until=simconfig.SIMULATION_TIME)

# Generating report
Report.generate_report(sys.argv[3])
