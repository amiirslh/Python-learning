from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        """This method should be impelementd"""
    @abstractmethod
    def repair(self):
        """this method should be implemented"""
    @classmethod
    def clsname(self):
        print(self.__name__)

class LandV(Vehicle):
    @abstractmethod
    def brake(self):
        """barke to stop land vehicle"""

class AirV(Vehicle):
    @abstractmethod
    def eject(self):
        """eject in danger"""


class Car(LandV):
    def __init__(self,name:str,year:int):
        self.name=name
        self.year=year
    def move(self):
        print('moving')
    def repair(self):
        print('repairng')
    def brake(self):
        print('braking')

class AirPlane(AirV):
    def move(self):
        print('flying')
    def repair(self):
        print('repairing in the air')

    def eject(self):
        print('ejecting')

b747=AirPlane()
benz=Car('s500',2021)