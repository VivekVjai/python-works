#sum of first n even numbers 
num1=2

num2=int(input("enter the last even number"))

sum=0

for i in range(2,num2+1,2):

    sum=i+sum

print(sum)