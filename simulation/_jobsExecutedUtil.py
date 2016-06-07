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

JOBS_EXECUTED = report['jobsExecutedOnNodes']
totalJobs = 0

for node in JOBS_EXECUTED:
    totalJobs += node.get('jobsExecuted')

