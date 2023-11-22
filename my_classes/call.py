class A:
    def __init__(self,x):
        self.x=x
    def __call__(self,x):
        print('amir')
        self.x=x
obj=A(5)
print(obj.x)
obj(1)
print(obj.x)