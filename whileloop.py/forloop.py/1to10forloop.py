#program to print 1 to 10

#syntax

#range(start,end-1,step)

#step=increment or decremenet


sequence=range(1,11,1)

for num in sequence:

    print(num)


#program to print 10 to 1

sequence=range(10,0,-1)

for num in sequence:

    print(num)


#variable define cheyyanda direct aay define cheyyam

for num in range(1,10,1):

    print(num)


#start and end 

start=int(input("enter the starting limit "))

end=int(input("enter the end limit"))

if start<end:

    for num in range(start,end+1,1):

        print(num)

else:

    for num in range(start,end-1,-1):

        print(num)

