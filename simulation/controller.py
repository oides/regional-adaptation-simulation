"""
Represents each node on distributed environment in charge of execute jobs.

"""
__author__ = 'Eudes Santos Andrade'


from report import Report
from controlfunctions import ControlFunctions
from environment import SimulationEnvironment
from region import Region
import simconfig
import copy


class Controller(object):

    def __init__(self, simpyEnvironment, simulationEnvironment, P=2.0, I=0.0, D=1.0, Derivator=0, Integrator=0, Integrator_max=5, Integrator_min=-5):

        self.simpyEnvironment = simpyEnvironment
        self.simulationEnvironment = simulationEnvironment
        self.lastCountIdleLoops = None

        self.Kp=P
        self.Ki=I
        self.Kd=D
        self.Derivator=Derivator
        self.Integrator=Integrator
        self.Integrator_max=Integrator_max
        self.Integrator_min=Integrator_min

        self.set_point=0.0
        self.error=0.0

    def startOperation(self):
        while True:
            yield self.simpyEnvironment.timeout(self.tunning())
            
    def tunning(self):
        idleLoops = self.simulationEnvironment.idleLoops;

        if self.lastCountIdleLoops is not None:
            controlledVariable = idleLoops - self.lastCountIdleLoops

            actuation_value = self.update(controlledVariable)

            self.simulationEnvironment.region.increment_region_size(actuation_value)
            Report.add_actuation(actuation_value, controlledVariable, self.simpyEnvironment.now)

        self.lastCountIdleLoops = idleLoops

        return simconfig.CONTROLLER_FREQUENCY


    def update(self,current_value):

        self.error = self.set_point - current_value

        self.P_value = self.Kp * self.error
        self.D_value = self.Kd * ( self.error - self.Derivator)
        self.Derivator = self.error

        self.Integrator = self.Integrator + self.error

        if self.Integrator > self.Integrator_max:
            self.Integrator = self.Integrator_max
        elif self.Integrator < self.Integrator_min:
            self.Integrator = self.Integrator_min

        self.I_value = self.Integrator * self.Ki

        PID = self.P_value + self.I_value + self.D_value

        return int(PID)

    def setPoint(self,set_point):
        """
        Initilize the setpoint of PID
        """
        self.set_point = set_point
        self.Integrator=0
        self.Derivator=0

    def setIntegrator(self, Integrator):
        self.Integrator = Integrator

    def setDerivator(self, Derivator):
        self.Derivator = Derivator

    def setKp(self,P):
        self.Kp=P

    def setKi(self,I):
        self.Ki=I

    def setKd(self,D):
        self.Kd=D

    def getPoint(self):
        return self.set_point

    def getError(self):
        return self.error

    def getIntegrator(self):
        return self.Integrator

    def getDerivator(self):
        return self.Derivator
