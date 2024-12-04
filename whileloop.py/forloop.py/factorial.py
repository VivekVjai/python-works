#print factorial of a number

num=int(input("enter the number:  "))

fact=1

for num in range(1,num+1,1):

    fact=fact*num

print(fact)

