#bank [acno,balance,ac_type,customer_name] [initialise,deposit(amount,withdraw(ammount),get_balance)]

class Bank:

    accountnumber=int
    balance=int
    accounttype=str
    customer_name=str

    def __init__(self,accountnumber,balance,accounttype,customer_name):

        self.accountnumber=accountnumber
        self.balance=balance
        self.accounttype=accounttype
        self.customer_name=customer_name

    def deposit(self,amount):

        self.balance+=amount

        print(f"your account {self.accountnumber} has been credited with amount {amount} avl balance {self.balance}")
              
    def withdraw(self,amount):

        if self.balance<amount:

            print("insufficient balance")

        else:

            self.balance-=amount

            print(f"your account {self.accountnumber} has been debited with amount {amount} aval balance {self.balance}")

    def get_balance(self):

        print("your available balance ", (self.balance))

customer_instance1=Bank(217711,10000,"savings","ramesh")

customer_instance1.withdraw(2000)

customer_instance1.get_balance()