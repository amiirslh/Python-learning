class Vehicle:
    def __init__(self,color='',speed=''):
        self.color=color
        self.speed=speed
class Airplane(Vehicle):
    def __init__(self,kind='',**kwargs):
        super().__init__(**kwargs)
        self.kind=kind
class Car(Vehicle):
    def __init__(self,kind='',**kwargs):
        super().__init__(**kwargs)
        self.kind=kind
    def move(self):
        print(f'the {__class__.__name__} move on the road')
class Bicycle(Vehicle):
    def __init__(self,size='',**kwargs):
        super().__init__(**kwargs)
        self.size=size
    def move(self):
        print(f'the {__class__.__name__} move on the sidewalk')

class Lambo(Car):
    def __init__(self,topspeed='',year='',**kwargs):
        super().__init__(**kwargs)
        self.topspeed=topspeed
        self.year=year

class Benz(Car):
    def __init__(self,topspeed='',year='',**kwargs):
        super().__init__(**kwargs)
        self.topspeed=topspeed
        self.year=year
    def move(self):
        print(f'the {__class__.__name__} move on the ground')


c200=Benz(topspeed='120mph',year='2021')
c200.move()
aventador=Lambo(topspeed='220mph',year='2020')
aventador.move()