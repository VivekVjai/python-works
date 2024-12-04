num1=int(input("enter the first number: "))

num2=int(input("enter the second number: "))

i=1   #highest commn diviser starts from 1

while(i<=num1 and i<=num2): #loopil rand condion simulataneouly check cheyyanom.
                             #"and " condition aayathinal ythelm orenam fail aayal lopp stop cheyyum
    
    if (num1%i==0 and num2%i==0):  #while loopil if condition state cheyth

        gcd=i
        
    i=i+1

print(gcd)