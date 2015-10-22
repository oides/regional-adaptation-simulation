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


def adicionarPerturbacao(simulationEnvironment):
    
    # Criando perturbações no ambiente
    while True:
        yield simpyEnvironment.timeout(simulationEnvironment.gerarNovaPerturbacao())
        
def adicionarNo(simulationEnvironment, identificador):
    
    novoNo = Node(simulationEnvironment, simpyEnvironment, identificador)
    novoNo.iniciarOperacao()
        

# Configuração e início da Simulação
print('Starting simulation')

# random.seed(RANDOM_SEED)  # Semente para reprodução de resultados
simulationEnvironment = Environment() # Criação do ambiente da simulação

# Criando o environment do simpy
simpyEnvironment = simpy.Environment()

# Registro de processos
simpyEnvironment.process(adicionarPerturbacao(simulationEnvironment)) # Processo que adiciona perturbação ao ambiente da simulação
novoNo = Node(simulationEnvironment, simpyEnvironment, '1')
simpyEnvironment.process(novoNo.iniciarOperacao()) # Processo que adiciona novo no ambiente da simulação

# Executando a simulação
simpyEnvironment.run(until=simconfig.SIMULATION_TIME)


# Exibindo número de jobs executados por cada nó...
print('Número de Jobs executados pelo nó ' + novoNo.identificador + ': ' + str(novoNo.numeroJobsExecutados))
