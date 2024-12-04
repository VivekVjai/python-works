def factorial(num):

    if num==0 or num<0:

        fact=1

        return fact



    elif num>0:

        fact=1

        for num in range(1,num+1):

             fact=num*fact

        return fact
    
def is_factorial():

    assert factorial(3)==6,"factorial check failed "

    assert factorial(0)==1,"factorial of zero chck failed "

    assert factorial(-3)==1,"factorial check of negative number failed"

try:

    is_factorial()

    print("test passed")

except Exception as e:

    print("test failed",e)