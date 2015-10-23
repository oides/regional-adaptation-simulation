"""
Simulação para avaliação do tradeoff existente entre overhead introduzido e a economia
de recursos computacionais após adoção de um planejamento regional adaptativo.

Objeto de adaptação: tamanho das regiões.

"""
__author__ = 'Eudes Santos Andrade'


import random

import simpy
import simconfig
from environment import SimulationEnvironment
from node import Node
from report import Report
from region import Region


def addDisturbing():
    simpyEnvironment.process(simulationEnvironment.startDisturbing())
        
        
def addNodes(amount):
        
    nodes = []
    
    for x in range(amount):
        newNode = Node(simpyEnvironment, simulationEnvironment, region, 'Node ' + str(x))
        nodes.append(newNode)
        simpyEnvironment.process(newNode.iniciarOperacao()) # Processo que adiciona novo no ambiente da simulação
        
    return nodes

# Configuração e início da Simulação
print('Starting simulation')

# Semente para reprodução de resultados
random.seed(simconfig.RANDOM_SEED)

# Criando o environment do simpy
simpyEnvironment = simpy.Environment()

# Building the simulation environment
simulationEnvironment = SimulationEnvironment(simpyEnvironment)

# Building the simulation region configuration
region = Region()

# Adding disturbing process
addDisturbing() # Processo que adiciona perturbação ao ambiente da simulação

# Adding node
nodes = addNodes(simconfig.NODES_NUMBER)

# Executando a simulação
simpyEnvironment.run(until=simconfig.SIMULATION_TIME)

# Generating report
Report.generateReport()