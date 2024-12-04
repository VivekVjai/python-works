num1=int(input("enter the number "))

num2=int(input("enter the number "))

try:

    result=num1/num2

    print(result)

except:

    num2=int(input("enter a number greater than zero"))

    result=num1/num2

    print(result)

finally:

    print("file write ")

    print("database commit ")            