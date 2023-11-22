class GetLoggerMixin:
    pass

class Animal:
    def __init__(self,name='',color=''):
        self.name=name
        self.color=color
    def move(self):
        print(f'{self.name} walks')
        
        
class Bird(Animal):
    def __init__(self,kind,**kwargs):
        super().__init__(**kwargs)
        self.kind=kind
    def move(self):
        print(f'{self.name} flys')
        
        
class Mamamls(Animal):
    def __init__(self,noo='',**kwargs):
        super().__init__(**kwargs)
        self.noo=noo
qor=Animal(name='qo',color='green')
qor.move()

kaftar=Bird(name='kaftarhafar',color='white',kind='persian')
kaftar.move()

cow=Mamamls(name='gaveahmad',color='brown', noo='british')
cow.move()