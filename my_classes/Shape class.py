class Shape:
    def __init__(self,**kwargs):
        self.enviroment=None
        self.area=None
        for key, value in kwargs.items():
            setattr(self,key,value)

    def calculate_area(self):
        pass


    def calculate_environment(self):
        pass

    def show(self):
        "show all attr in init class"
        info=''
        for key , value in self.__dict__.items():
            #if value>0:
                info+=f'{key}:{value}\n'
        print(info)
    def __str__(self):
        return f'***{self.__class__.__name__}***'

class Rectangle(Shape):
    def __init__(self,**kwrags):
        super().__init__(**kwrags)

    def calculate_environment(self):
        self.enviroment=2*(self.arz+self.tool)
    @property
    def calculate_area(self):
        self.area=self.arz*self.tool
class Circle(Shape):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def calculate_environment(self):
        self.enviroment = self.sh * self.sh * self.p

    def calculate_area(self):
        self.area=self.q*self.p


rec=Rectangle(arz=5,tool=10)
rec.calculate_area
print(rec.area)