from datetime import datetime

class Product:
    def __init__(self,product_name,price,off,*args):
        self.product_name=product_name
        self.price=price*off/100
        self.off=off
    def __str__(self):
        return self.product_name

class Comment(Product):
    website_name='Sabzlearn.ir'
    def __init__(self , product_kind,name,description,like,dislike,*args):
        super().__init__(*args)
        self.product_kind=product_kind
        self.name=name
        self.description=description
        self.date=datetime.now()
        self.like=like
        self.dislike=dislike

    def show(self):
        print(f"Product_kind={self.product_kind}\n"
               f"price={self.price}\n"
               f"name:{self.name}\n"
               f"description:{self.description}\n"
               f"date={self.date}\n"
               f"like_count:{self.like}\n"
               f"dislike:{self.dislike}\n")



def main():
    p1=Product('py',100,50,)
    c1=Comment('','amir','ridi',100,50,p1)
    c1.show()
if __name__ == "__main__":
    main()
