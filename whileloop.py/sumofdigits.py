#sum of digits

num=int(input("enter the number:  "))

sum=0

while(num!=0):

    div=num%10

    sum=sum+div

    num=num//10

print(sum)

