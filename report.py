"""
Implements the simulation report.

"""
__author__ = 'Eudes Santos Andrade'


import yaml


class Report(object):

    content = {}

    jobsExecutedOnNodes = []
    disturbings = []
    
    def addJobsExecutedOnNodes(nodeId):
        
        jobsExecutedOnNodesDictionary = {jobsOnNode['nodeId']: jobsOnNode for jobsOnNode in Report.jobsExecutedOnNodes}
        
        jobOnNode = jobsExecutedOnNodesDictionary.get(nodeId, None)

        if jobOnNode is not None:
            jobOnNode['jobsExecuted'] = jobOnNode['jobsExecuted'] + 1
        else:
            newJobsOnNode = {}
            newJobsOnNode['nodeId'] = nodeId
            newJobsOnNode['jobsExecuted'] = 1
            Report.jobsExecutedOnNodes.append(newJobsOnNode)

    def addDisturbing(disturbingLevel, disturbingDuration):
        
        disturbing = {}
        disturbing['disturbingLevel'] = disturbingLevel
        disturbing['disturbingDuration'] = disturbingDuration
        
        Report.disturbings.append(disturbing)
        
    def generateReport():
        
        generatedFile = open('generatedreport.yaml', 'w')
        
        Report.content['disturbings'] = Report.disturbings
        Report.content['jobsExecutedOnNodes'] = Report.jobsExecutedOnNodes
        
        yaml.dump(Report.content, generatedFile)
