from dataclasses import dataclass,InitVar
@dataclass
class Person:
    name:str
    family:str
    age:int
    gender:InitVar[str]
    def __post_init__(self,gender):
        if gender == 'man' :
            self.name+='*'
p=Person(name='amir',family='salehi',age=16,gender='man')
print(p)
print(type(p))
@dataclass
class A:
    name:str
hasan=A('hasan')
print(hasan)