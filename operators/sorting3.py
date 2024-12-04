num1=int(input("enter the number "))
num2=int(input("enter the number "))
num3=int(input("enter the number "))

if num1<num2<num3:

    print(num1,num2,num3)

elif num1>num2>num3:

    print(num3,num2,num1)

elif num1<num2>num3 and num1>num3:

    print(num3,num1,num2)

elif num1<num2>num3 and num3>num1:

    print(num1,num3,num2)

elif num1>num2<num3 and num1>num3:

    print(num2,num3,num1)

elif num1>num2<num3 and num3>num1:

    print(num2,num1,num3)

