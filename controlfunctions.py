"""
Implements the control functions used on simulation.

"""
__author__ = 'Eudes Santos Andrade'


import simconfig


class ControlFunctions(object):
    
    def calculate_job_cost(disturbind_level, region_size):
        job_cost = disturbind_level - region_size
        
        if job_cost < 1:
            job_cost = 1
            
        print('Job Cost: ' + str(job_cost))
        return job_cost
 
    def calculate_actuation_value(controlled_variable_number_jobs_executed):
        
        if controlled_variable_number_jobs_executed == simconfig.SET_POINT:
            return 0
        elif controlled_variable_number_jobs_executed < simconfig.SET_POINT:
            return 1
        else:
            return -1
 
