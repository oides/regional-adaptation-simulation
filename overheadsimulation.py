"""
Simulação para avaliação do tradeoff existente entre overhead introduzido e a economia
de recursos computacionais após adoção de um planejamento regional adaptativo.

Objeto de adaptação: tamanho das regiões.

"""
__author__ = 'Eudes Santos Andrade'


import random

import simpy
import simconfig


class Ambiente(object):
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


class No(object):
    """
    Representa cada nó que realiza trabalho no ambiente distribuído.
    """
    def __init__(self, ambiente, identificador):
        self.identificador = identificador
        self.ambiente = ambiente    # Mantem localmente informações do ambiente sob o qual o nó está inserido
        self.numeroJobsExecutados = 0

    def iniciarOperacao(self):
        while True:
            yield env.timeout(self.executarTrabalho())
            
    def executarTrabalho(self):
            self.numeroJobsExecutados += 1
            return ambiente.NIVEL_ATUAL_PERT
            

def adicionarPerturbacao(ambiente):
    
    # Criando perturbações no ambiente
    while True:
        yield env.timeout(ambiente.gerarNovaPerturbacao())
        
def adicionarNo(ambiente, identificador):
    
    novoNo = No(ambiente, identificador)
    novoNo.iniciarOperacao()
        

# Configuração e início da Simulação
print('Starting simulation')

# random.seed(RANDOM_SEED)  # Semente para reprodução de resultados
ambiente = Ambiente() # Criação do ambiente da simulação

# Criando o enviroment do simpy
env = simpy.Environment()

# Registro de processos
env.process(adicionarPerturbacao(ambiente)) # Processo que adiciona perturbação ao ambiente da simulação
novoNo = No(ambiente, '1')
env.process(novoNo.iniciarOperacao()) # Processo que adiciona novo no ambiente da simulação

# Executando a simulação
env.run(until=simconfig.SIMULATION_TIME)


# Exibindo número de jobs executados por cada nó...
print('Número de Jobs executados pelo nó ' + novoNo.identificador + ': ' + str(novoNo.numeroJobsExecutados))
