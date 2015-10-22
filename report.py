"""
Implements the simulation report.

"""
__author__ = 'Eudes Santos Andrade'


import yaml


class Report(object):

    jobsExecutedOnNodes = {}
    
    def addJobsExecutedOnNodes(nodeId):
        
        jobOnNode = Report.jobsExecutedOnNodes.get(nodeId, None)
        
        if jobOnNode is None:
            Report.jobsExecutedOnNodes[nodeId] = 1
        else:
            Report.jobsExecutedOnNodes[nodeId] = jobOnNode + 1

    def generateReport():
        
        generatedFile = open('generatedreport.yaml', 'w')
        
        yaml.dump(Report.jobsExecutedOnNodes, generatedFile)
        yaml.dump(Report.jobsExecutedOnNodes, generatedFile)
        yaml.dump(Report.jobsExecutedOnNodes, generatedFile)
        yaml.dump(Report.jobsExecutedOnNodes, generatedFile)
        yaml.dump(Report.jobsExecutedOnNodes, generatedFile)
        yaml.dump(Report.jobsExecutedOnNodes, generatedFile)
