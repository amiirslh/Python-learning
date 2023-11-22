from datetime import datetime
from pprint import pprint
class Product:
    def __init__(self,product_name,price,off):
        self.product_name=product_name
        self.price=price
        self.oaff=off

#class name:

    def __str__(self):
        return self.product_name
class Comment:
    website_name='Sabzlearn.ir'
    def __init__(self , product_kind,name,description,like,dislike):
        self.product_kind=product_kind
        self.name=name
        self.description=description
        self.date=datetime.now()
        self.like=like
        self.dislike=dislike

    def show(self):
        print(f"Product_kind={self.product_kind}\n"
               f"name:{self.name}\n"
               f"description:{self.description}\n"
               f"date={self.date}\n"
               f"like_count:{self.like}\n"
               f"dislike:{self.dislike}\n")


    @classmethod
    def info(cls):
        print(f'website name : {cls.website_name}')

    @classmethod
    def sanasor(cls,product_kind,name,description,like,dislike):
        sc=description.replace('fuck','****')
        return cls(product_kind,name,sc,like,dislike)

    @staticmethod
    def infooo(time):
        pass



def main():
    product=Product('py course',400,100)
    c1=Comment.sanasor(product,'amir',' so fucked up',100,50)


    c1.show()
if __name__ == "__main__":
    main()
