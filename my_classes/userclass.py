from typing import List
from pprint import pprint
class UserList(list):
    def search(self,username:str):
        matching_user=[]
        for user in self:
            if username in user.username:
                matching_user.append(user)
        return matching_user
    def append(self,obj):
        if not isinstance(obj,User):
            raise TypeError('RIDI')
        return super().append(obj)


class User:
    all_user=UserList()
    def __init__(self,username,email,age:int,**kwargs):
        self.username=username
        self.email=email
        self.age=age
        User.all_user.append(self)

    def __str__(self):
        return(f'{self.username} {self.email} {self.age}')


    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.username}' '{self.email}' '{self.age}')")


class Seller(User):
    def __init__(self,shaba,**kwargs):
        super().__init__(**kwargs)
        self.shaba=shaba
    def order(self,order:'Order')-> None:
        pass

class Buyer(User):

    def __init__(self,phone,**kwargs):
        super().__init__(**kwargs)
        self.phone=phone

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.username}' '{self.email}' '{self.age}' '{self.phone}')")


class Seller_Buyer(Seller,Buyer):
    def __init__(self,score,**kwargs):
        super().__init__(**kwargs)
        self.score=score

def main():
    amir=Seller_Buyer(age=12,username='salehi',phone='09126872056',score=123,email='amir1999@gamil.com',shaba=1212128127278387388)
    amir=Seller_Buyer(age=12,username='salehiii',phone='09126872056',score=123,email='amir1999@gamil.com',shaba=1212128127278387388)
    print(amir.score)
    print(Seller_Buyer.all_user.search('salehi'))


if __name__ == '__main__':
    main()

