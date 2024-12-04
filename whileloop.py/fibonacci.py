#sequence in which each number is the sum of the two preceeding ones.
# 0,1,1,2,3,5,8,13,21,.....

num=int(input("enter the number to which you want fibonacci series: "))

a,b=0,1

while(b<=num):

    print(b)  #here print b is first because we have to print the initial value of b and b gives the fibonacci series  

    a=b

    b=a+b

print ("done")

