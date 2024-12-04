num=int(input("enter the number "))

total=0

for i in range(1,num,):

    if num%i==0:

        total+=i

print("total=", total)

print("perfect" if total==num else "not perfect")

