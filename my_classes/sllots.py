class MyClass:
    __slots__ = ('a','b')
    def __init__(self,a,b):
        self.a=a
        self.b=b
class C(MyClass):
    def __init__(self,a,b):
        super().__init__(a,b)


