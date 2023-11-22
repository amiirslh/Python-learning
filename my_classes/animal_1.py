class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def info(self):
        print(f'Hello Iam an animal. My name is {self.name} and Iam {self.color}')
    def make_sound(self):
        print('genertic animal sounds')
class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name,color)
    def info(self):
        print(f'Hello i,am a cat my name is {self.name} and  I look {self.color}')

    def make_sound(self):
        print('meow')


class Cow(Animal):
    def __init__(self,name,color):
        super().__init__(name,color)
    def info(self):
        print(f'Hello i,am a cow my name is {self.name} and iam {self.color}')

    def make_sound(self):
        print('Mooooow')


pillow=Cat('pillow','black')

cow=Cow('brad','brown')

for animal in [pillow,cow]:

    animal.make_sound()
    animal.info()
dog=Animal('maya','white')
dog.info()
dog.make_sound()