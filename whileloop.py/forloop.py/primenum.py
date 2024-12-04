#prime number 

number=int(input("enter the number to be checked "))


is_prime=True

for i in range (2,number-1,):  #1 and that given number itself should the multiple so excluding 1 & number 

    if number%i==0:

        is_prime=False

        break

print(is_prime)