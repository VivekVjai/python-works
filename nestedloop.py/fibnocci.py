num1=0
num2=1
print(num1)
print(num2)

for row in range(1,7):
    num3=num2+num1
    print(num3)
    num1=num2
    num2=num3

    for column in range(1,row+1):
        
        print(num3,end="\t")