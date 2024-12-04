num1=int(input("enter the number "))

num2=int(input("enter the second number "))

num3=int(input("enter the third number "))

if num1>num2>num3:

    print(f"{num1} is greater")

elif num2>num3:

    print(f"{num2} is greater")

elif num1==num2==num3:

    print("all are equal")

else:

    print(f"{num3} is greater")

    
