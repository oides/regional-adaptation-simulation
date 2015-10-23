"""
Implements the region defined on regional planner pattern.

"""
__author__ = 'Eudes Santos Andrade'


import simconfig


class Region(object):
    
    def __init__(self):
        self.region_size = simconfig.DEFAULT_REGION_SIZE;
 
