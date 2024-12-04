class Car:

    name:str
    brand:str
    fueltype:str

    def __init__(self,name,brand,fueltype):

        self.name=name
        self.brand=brand
        self.fueltype=fueltype

    def display(self):

        print(self.name,self.brand,self.fueltype)

    def __str__(self):

        return self.name

car_instance1=Car("swift","suzuki","petrol")

car_instance1.display()

print(car_instance1)


#__str__ --> oru objectntae string representationu vendiyittu use cheyunnu 
#__str__ use cheythu nammal nthano return cheyunnath ath print(carinstance1) kodukumbol print aakum
#string value mathramae return cheyyan patukayullu



