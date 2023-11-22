class Personnnn:
    def __init__(self,name,lname,age,national_code):
        self.name=name.capitalize()
        self.lname=lname.capitalize()
        self.age=age
        self.national_code=national_code
    def __add__(self,s_obj):
        return self.age + s_obj.age

    def __gt__(self,s_obj):
        if self.age > s_obj.age:
            return(f'{self.name} is bigger than {s_obj.name}')
        else:
            return(f'{self.name} is smaller than {s_obj.name}')
    def __eq__(self,s_obj):
        return self.national_code == s_obj.national_code

    def __str__(self):
        return f'{self.name} {self.lname} ,Age: {self.age}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}' '{self.lname}' {self.age}')"

person1=Personnnn('ali','vaezi',23,'0024033138')
person2=Personnnn('amir','salehi',50,'002133121')
print(person2+person1)
print(person1 == person2)
print(person2 != person1)

