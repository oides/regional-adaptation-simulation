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
            
        return job_cost
 
