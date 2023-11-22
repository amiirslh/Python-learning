class NameField:
    def __set_name__(self, owner, name):
        self.name=name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if 0<len(value)<10:
            instance.__dict__[self.name]=value
        else:
            raise ValueError('not enough char to creat a name object')
    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Parnet:

    def __init__(self,child,mother,father):
        self.child_name=child
        self.mother_name=mother
        self.father_name=father


amir=Parnet('amir','parvaneh','manuch')
print(amir.child_name)
print(amir.mother_name)
print(amir.father_name)
print(amir.__dict__)
