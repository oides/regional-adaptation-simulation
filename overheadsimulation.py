"""
Simulação para avaliação do tradeoff existente entre overhead introduzido e a economia
de recursos computacionais após adoção de um planejamento regional adaptativo.

Objeto de adaptação: tamanho das regiões.

"""
__author__ = 'Eudes Santos Andrade'


import random

import simpy
import simconfig
from environment import Environment
from node import Node
from report import Report


def addDisturbing():
    simpyEnvironment.process(startDisturbing())
        
def startDisturbing():
    
    # Criando perturbações no ambiente
    while True:
        yield simpyEnvironment.timeout(simulationEnvironment.generateDisturbing())
        
def addNodes(amount):
        
    nodes = []
    
    for x in range(amount):
        newNode = Node(simulationEnvironment, simpyEnvironment, 'Node ' + str(x))
        nodes.append(newNode)
        simpyEnvironment.process(newNode.iniciarOperacao()) # Processo que adiciona novo no ambiente da simulação
        
    return nodes

# Configuração e início da Simulação
print('Starting simulation')

# random.seed(RANDOM_SEED)  # Semente para reprodução de resultados
simulationEnvironment = Environment() # Criação do ambiente da simulação

# Criando o environment do simpy
simpyEnvironment = simpy.Environment()

# Adding disturbing process
addDisturbing() # Processo que adiciona perturbação ao ambiente da simulação

# Adding node
nodes = addNodes(simconfig.NODES_NUMBER)

# Executando a simulação
simpyEnvironment.run(until=simconfig.SIMULATION_TIME)

# Generating report
Report.generateReport()

