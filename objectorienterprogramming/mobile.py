class Mobile:

    name:str
    price:int
    brand:str

    def __init__(self,name,price,brand):

        self.name=name
        self.brand=brand
        self.price=price

    def display(self):

        print(self.name,self.brand,self.price) 

mobile_instance1=Mobile("samsungs23",70000,"samsung")

mobile_instance1.display()
