#largest digit in a number 

num=int(input("enter the number:  "))

number=num

i=1

while(num>0):

    rem=num%10

    i=max(i,rem)

    num=num//10

print("greatest digit in the number is ",i)