class Color:
    def __init__(self,rgb,name):

        self.rgb=rgb
        self.name=name
    def __str__(self):
        return f' the color details: {self.rgb},{self.name}'
    def __repr__(self):
        return (f'{self.rgb},{self.name}')

    @property

    def name(self):


        return self._name

    @name.setter
    def name(self, name):

        if name:
            self._name = name
        else:
            raise ValueError('ivalid name')
    @name.deleter
    def name(self):

        del self._name


c2=Color(0x67653,'red')
print(c2)
c2.name='blue'
print(c2.name)
print(c2)