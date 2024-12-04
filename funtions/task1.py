#create a funtion smart_sub with three parameters num1,num2,reverse 
#reverse take boolean values
#if reverse==true then return num2-num1 else return num1-num2

def smart_sub(num1,num2,reverse):

    return num2-num1 if reverse==True else num1-num2

print (smart_sub(10,5,True))