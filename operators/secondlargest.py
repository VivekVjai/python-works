num1=int(input("enter the number "))

num2=int(input("enter the number "))

num3=int(input("enter the number "))

if num1<num2<num3:

    print(f"{num2} is the 2nd largest")

elif num1>num2>num3:

    print(f"{num2} is the 2nd largest")

elif num1<num2>num3:

    if num1>num3:

        print(f"{num1} is second largest ")

    else:

         print(f"{num3} is second largest")

elif num1>num2<num3:

    if num1>num3:

       print(f"{num3} is 2nd lagest")
       
    else:

        print(f"{num1} is 2nd largest")


