"""
Utilitário para suporte a execução da simulacao.

"""
__author__ = 'Eudes Santos Andrade'


import yaml
import sys


if sys.argv[1] == 'enabled':
    f = open('reports/generatedreport.yaml', 'r')
else:
    f = open('reports/generatedreportControlerDisabled.yaml', 'r')

report = yaml.load(f)

print(str(report['idle_cycles']))


