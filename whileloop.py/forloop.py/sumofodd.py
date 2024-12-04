num1=int(input("enter the starting odd limit "))

num2=int(input("enter the ending odd limit "))

sum=0

for i in range(num1,num2+1,2):

    sum=i+sum
    
print(sum)