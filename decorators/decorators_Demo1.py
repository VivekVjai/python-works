def swap_decorator(fn):

    def wrapper(n1,n2):
        n1=round(n1)
        n2=round(n2)

        if n1<n2:

            (n1,n2)=(n2,n1)

        return fn(n1,n2)
    return wrapper

#def round_dec(fn):

    #def wrapper(n1,n2):
        
        #n1=round(n1)
        #n2=round(n2)
        #return fn(n1,n2)
    #return wrapper

@swap_decorator
#@round_dec
def add_num(num1,num2):

    return num1+num2

@swap_decorator
#@round_dec
def sub_num(num1,num2):

    return num1-num2

@swap_decorator
#@round_dec
def div_num(num1,num2):

    return num1/num2

print(div_num(2,10))

print(add_num(2.5,3.6))