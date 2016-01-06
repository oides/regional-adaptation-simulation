"""
Implements the region defined on regional planner pattern.

"""
__author__ = 'Eudes Santos Andrade'


import simconfig
from report import Report


class Region(object):
    
    def __init__(self, simpyEnvironment):
        self._region_size = simconfig.DEFAULT_REGION_SIZE;
        self.simpyEnvironment = simpyEnvironment

    
    def increment_region_size(self, actuation_value):
        self._region_size += actuation_value
        Report.add_region_size(self._region_size, self.simpyEnvironment.now)
        
 
    