import logging



class Animal:
    def __init__(self,name:str,kind:str,**kwargs):
        self.name=name
        self.kind=kind

    def make_sound(self):
        print('Generic animal sound')


class Mammal(Animal):
    def __init__(self,legs:int,**kwargs):
        super().__init__(**kwargs)
        self.legs=legs
    def make_sound(self):

        print('Generic mammal sound')


class Dog(Mammal):
    def __init__(self,nejad:str,**kwargs):
        super().__init__(**kwargs)
        self.nejad=nejad
    def make_sound(self):

        print('woof')


pillow=Dog(nejad='dsh',legs=4,name='pillow',kind='gorbe')
cow=Mammal(legs=10,name='sanaz',kind='norwey',)
cow.make_sound()
