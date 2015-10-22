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


class No(object):
    """
    Representa cada nó que realiza trabalho no ambiente distribuído.
    """
    def __init__(self, environment, identificador):
        self.identificador = identificador
        self.environment = environment    # Mantem localmente informações do ambiente sob o qual o nó está inserido
        self.numeroJobsExecutados = 0

    def iniciarOperacao(self):
        while True:
            yield env.timeout(self.executarTrabalho())
            
    def executarTrabalho(self):
            self.numeroJobsExecutados += 1
            return self.environment.NIVEL_ATUAL_PERT
            

def adicionarPerturbacao(environment):
    
    # Criando perturbações no ambiente
    while True:
        yield env.timeout(environment.gerarNovaPerturbacao())
        
def adicionarNo(environment, identificador):
    
    novoNo = No(environment, identificador)
    novoNo.iniciarOperacao()
        

# Configuração e início da Simulação
print('Starting simulation')

# random.seed(RANDOM_SEED)  # Semente para reprodução de resultados
environment = Environment() # Criação do ambiente da simulação

# Criando o environment do simpy
env = simpy.Environment()

# Registro de processos
env.process(adicionarPerturbacao(environment)) # Processo que adiciona perturbação ao ambiente da simulação
novoNo = No(environment, '1')
env.process(novoNo.iniciarOperacao()) # Processo que adiciona novo no ambiente da simulação

# Executando a simulação
env.run(until=simconfig.SIMULATION_TIME)


# Exibindo número de jobs executados por cada nó...
print('Número de Jobs executados pelo nó ' + novoNo.identificador + ': ' + str(novoNo.numeroJobsExecutados))
