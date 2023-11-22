class Personnnn:
    def __init__(self,name,lname,age):
        self.name=name.capitalize()
        self.lname=lname.capitalize()
        self.age=age


    def __str__(self):
        return f'{self.name} {self.lname} ,Age: {self.age}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}' '{self.lname}' {self.age}')"

def main():
    person1=Personnnn('amir','salehi',12)
    print(person1)
    print(repr(person1))
if __name__ == '__main__':
    main()
