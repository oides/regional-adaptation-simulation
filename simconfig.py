"""
Simulação para avaliação do tradeoff existente entre overhead introduzido e a economia
de recursos computacionais após adoção de um planejamento regional adaptativo.

Objeto de adaptação: tamanho das regiões.

"""
__author__ = 'Eudes Santos Andrade'


import yaml


f = open('simconfig.yaml', 'r')

config = yaml.load(f)

print('Loading configuration...')

SIMULATION_TIME = config['SIMULATION_TIME']
RANDOM_SEED = config['RANDOM_SEED']
JOBS_NUMBER = config['JOBS_NUMBER']
NODES_NUMBER = config['NODES_NUMBER']
DEFAULT_REGION_SIZE = config['DEFAULT_REGION_SIZE']
CONTROLLER_FREQUENCY = config['CONTROLLER_FREQUENCY']