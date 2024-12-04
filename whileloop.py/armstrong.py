num=int(input("enter the number:  "))

number=num

sum=0

count=len(str(number))

while(num!=0):

    rem=num%10

    sum=(rem**count)+sum

    num=num//10

if(sum==number):

    print(number," is an armstrong number")

else:

    print(number," is not an armstrong number")

    
