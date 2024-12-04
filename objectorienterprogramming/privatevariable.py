

class Bankaccount:

    customer_name:str
    mpin:int
    accounttype:str

    def __init__(self,customer_name,mpin,accounttype):

        self.customer_name=customer_name

        self.__mpin=mpin  #__ double underscope koduthal private attribite aaay marum private aaki kazhinjal athinae clasinu ullil mathrame acess cheyyan pattu

        self.accounttype=accounttype

    def __str__(self):

        return self.customer_name

    def get_mpin(self):  #private aakiya attributinae print cheyyan claasinu akathu method define cheyyanaom allathae clasinu purathunu patilla

        print(self.__mpin)
    
bankaccount_instance=Bankaccount("hari",3456,"personal")

print(bankaccount_instance)

print(bankaccount_instance.accounttype)

bankaccount_instance.get_mpin()
