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

# Simulation
ENABLE_SEED = config['ENABLE_SEED']
RANDOM_SEED = config['RANDOM_SEED']

SIMULATION_TIME = config['SIMULATION_TIME']
NODES_NUMBER = config['NODES_NUMBER']
DEFAULT_REGION_SIZE = config['DEFAULT_REGION_SIZE']

# Controller
CONTROLLER_FREQUENCY = config['CONTROLLER_FREQUENCY']
SET_POINT = config['SET_POINT']

# Disturbing
BASE_DISTURBING_PERIOD = config['BASE_DISTURBING_PERIOD']
INTERVAL_DISTURBING_PERIOD = config['INTERVAL_DISTURBING_PERIOD']
BASE_DISTURBING_LEVEL = config['BASE_DISTURBING_LEVEL']
INTERVAL_DISTURBING_LEVEL = config['INTERVAL_DISTURBING_LEVEL']
