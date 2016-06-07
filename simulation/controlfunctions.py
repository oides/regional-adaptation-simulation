"""
Implements the control functions used on simulation.

"""
__author__ = 'Eudes Santos Andrade'


import simconfig
from report import Report
import random


class ControlFunctions(object):
    
    simpyEnvironment = None
    
    def calculate_job_cost(disturbind_level, region_size):
        job_cost = disturbind_level - region_size

        erlang_cost = random.gammavariate(simconfig.ERLANG_SHAPE, 1)
        job_cost += int(erlang_cost)

        if job_cost < 1:
            job_cost = 1
            
        Report.add_jobs_costs(job_cost, ControlFunctions.simpyEnvironment.now)
        return job_cost
 
    def calculate_actuation_value(controlled_variable_number_jobs_executed):
        
        error = simconfig.SET_POINT - controlled_variable_number_jobs_executed

        return error