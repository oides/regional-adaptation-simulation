"""
Implements the simulation report.

"""
__author__ = 'Eudes Santos Andrade'


import yaml


class Report(object):

    content = {}

    disturbings = []
    jobsExecutedOnNodes = []
    jobs_costs = []
    actuations = []
    region_sizes = []
    idle = 0

    def add_jobs_executed_on_nodes(node_id):
        
        jobsExecutedOnNodesDictionary = {jobsOnNode['nodeId']: jobsOnNode for jobsOnNode in Report.jobsExecutedOnNodes}
        
        jobOnNode = jobsExecutedOnNodesDictionary.get(node_id, None)

        if jobOnNode is not None:
            jobOnNode['jobsExecuted'] = jobOnNode['jobsExecuted'] + 1
        else:
            newJobsOnNode = {}
            newJobsOnNode['nodeId'] = node_id
            newJobsOnNode['jobsExecuted'] = 1
            Report.jobsExecutedOnNodes.append(newJobsOnNode)

    def add_jobs_costs(job_cost_value, current_time):
        
        job_cost = {}
        job_cost['job_cost_value'] = job_cost_value
        job_cost['current_time'] = current_time
        
        Report.jobs_costs.append(job_cost)

    def add_disturbing(disturbingLevel, disturbingDuration, currentTime):
        
        disturbing = {}
        disturbing['disturbingLevel'] = disturbingLevel
        disturbing['disturbingDuration'] = disturbingDuration
        disturbing['currentTime'] = currentTime
        
        Report.disturbings.append(disturbing)
        
    def add_actuation(actuation_value, controlled_variable, current_time):
        
        actuation = {}
        actuation['actuation_value'] = actuation_value
        actuation['controlled_variable'] = controlled_variable
        actuation['current_time'] = current_time
        
        Report.actuations.append(actuation)
        
    def add_region_size(region_size_value, current_time):
        
        region_size = {}
        region_size['region_size_value'] = region_size_value
        region_size['current_time'] = current_time
        
        Report.region_sizes.append(region_size)
        
    def add_idle_cycle():

        Report.idle += 1

    def generate_report(controllerEnabled):

        if controllerEnabled == 'enabled':
            fileName = 'generatedReport.yaml'
        else:
            fileName = 'generatedreportControlerDisabled.yaml'

        print('Generating report...')
        generatedFile = open('reports/' + fileName, 'w')
        
        Report.content['disturbings'] = Report.disturbings
        Report.content['jobsExecutedOnNodes'] = Report.jobsExecutedOnNodes
        Report.content['jobs_costs'] = Report.jobs_costs
        Report.content['actuations'] = Report.actuations
        Report.content['region_sizes'] = Report.region_sizes
        Report.content['idle_cycles'] = Report.idle

        yaml.dump(Report.content, generatedFile)
