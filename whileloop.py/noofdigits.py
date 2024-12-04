#count the no of digits

num=int(input("enter the number:  "))

count=0

while(num>0):

    count=count+1

    num=num//10
    
    
print(count)



