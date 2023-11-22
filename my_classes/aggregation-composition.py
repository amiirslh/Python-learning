class Qu:
    def __init__(self,q,a):
        self.q=q
        self.a=a
    def __str__(self):
        return f'{self.q},{self.a}'
class EP:
    def __init__(self):
        self.questiono=Qu('water boils at which degrees:',[100,90,85])
    def __str__(self):
        return f'{self.questiono.q},{self.questiono.a}'

e=EP()
print(e)