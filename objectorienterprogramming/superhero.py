class Superhero:

    name:str
    suit:str

    def __init__(self,name,suit):

        self.name=name
        self.suit=suit

    def __str__(self):

        return self.name
    
class Spiderman(Superhero):  #parent classil costructor define cheythittundenkil child classilum constructornae call cheythirikkanam

    def __init__(self,name,suit):

        super().__init__(name,suit) #parent class costructor calling  super(). refers to parentclass

    def super_power(self):

        print("spider sense","web shooting")

spiderman_instance=Spiderman("spiderman","spidersuit")

class Minnalmurali(Superhero):

    def __init__(self,name,suit):

        super().__init__(self,name,suit)

    def sper_power(self):

        print("running","reflexes")

minnalmurali_instance=Minnalmurali("minnal murali","minnal suit")

