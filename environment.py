"""
Implements the simulation environment meta-information.

"""
__author__ = 'Eudes Santos Andrade'


import random


class Environment(object):
    """
    Representa o ambiente do sistema distribuído a ser gerenciado.
    """
    def __init__(self):
        self.T_INTER_PERT = 5    # Cria uma nova perturbacão a cada 4 minutos
        self.T_VAR_INTER_PERT = 3  # Intervalo de variação do instante de criação de nova perturbação
        self.NIVEL_BASE_PERT = 5 # Define o nível da perturbação inserida no ambiente
        self.VAR_NIVEL_BASE_PERT = 4 # Define o nível da perturbação inserida no ambiente
        self.NIVEL_ATUAL_PERT = self.NIVEL_BASE_PERT # Define o nível da perturbação inserida no ambiente

    def gerarNovaPerturbacao(self):
        print('##########################################')
        print('######## GERANDO NOVA PERTURBACAO ########')
        print('##########################################')        
        
        self.NIVEL_ATUAL_PERT = random.randint(self.NIVEL_BASE_PERT-self.VAR_NIVEL_BASE_PERT, self.NIVEL_BASE_PERT+self.VAR_NIVEL_BASE_PERT)
        print('# Novo nível da perturbação: ' + str(self.NIVEL_ATUAL_PERT))
        
        intervaloProximaPerturbacao = random.randint(self.T_INTER_PERT-self.T_VAR_INTER_PERT, self.T_INTER_PERT+self.T_VAR_INTER_PERT)
        print('# Gerando nova perturbação em ' + str(intervaloProximaPerturbacao) + ' minutos')
        print('##########################################\n')        
        
        return intervaloProximaPerturbacao
