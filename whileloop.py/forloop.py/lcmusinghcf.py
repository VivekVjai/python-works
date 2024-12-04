#the relation between two numbers(num1,num2) and their  lcm and hcf 

#hcf*lcm=num1*num2

#so if we know hcf then lcm=(num1*num2)//hcf

num1=int(input("enter the first number "))

num2=int(input("enter the second number "))

gcd=1

min_num=num1 if num1<num2 else num2

for i in range (1,min_num+1):

    if (num1%i==0 and num2%i==0):

        gcd=i

print ("hcf of the two numbers is ",gcd)

lcm=(num1*num2)//gcd

print("lcm of the two numbers is ", lcm)

