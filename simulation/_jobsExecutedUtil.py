"""
Utilitário para suporte a execução da simulacao.

"""
__author__ = 'Eudes Santos Andrade'


import yaml

f = open('reports/generatedreport.yaml', 'r')

report = yaml.load(f)

JOBS_EXECUTED = report['jobsExecutedOnNodes']
totalJobs = 0

for node in JOBS_EXECUTED:
    totalJobs += node.get('jobsExecuted')

print(str(totalJobs))


