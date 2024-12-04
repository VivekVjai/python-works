class Shipping:

    def shipping_cost(self,weight):

        print(weight*5)

class Express_shipping(Shipping):

    def shipping_cost(self,weight):

        print(weight*20)

class Standard_shipping(Shipping):

    def shipping_cost(self, weight):

        print(weight*10)

Express_shipping_instance=Express_shipping()

Express_shipping_instance.shipping_cost(10)

Standard_shipping_instance=Standard_shipping()

Standard_shipping_instance.shipping_cost(10)
        

