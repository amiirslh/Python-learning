class PrintInfoMixin:
    def print_info(self):
        return f'{self.__class__.__name__},'
        pass
class Animal:
    def __init__(self,name:str,kind:str,**kwargs):
        self.name=name
        self.kind=kind

    def make_sound(self):
        print('Generic animal sound')


class Mammal(Animal,PrintInfoMixin):
    def __init__(self,legs:int,**kwargs):
        super().__init__(**kwargs)
        self.legs=legs
    def make_sound(self):

        print('Generic mammal sound')

cow=Mammal(name='brad',kind='british',legs=4)
cow.make_sound()
print(cow.print_info())
