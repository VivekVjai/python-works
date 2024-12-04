#program to check a given number is a primenumber or not

num=int(input("enter the number:  "))

factor=0

i=2

while(i<num):

    if(num%i==0): #if its true means i is a factor of the number 
                  #2 thottu <num vera ulla numbers check cheyyum athu satisfied ayatilla nkil while loop fail aakum else print aakum

        print(i)   #printing the factors of the number 

        factor=factor+1  #since it is in while loop the loop checks the same for i<num so the factors get added 
                         #and ee factor ntae value nokyattanu next if statement work akunnathu
    i=i+1

if(factor==0):

    print(num," is a prime number")

else:

    print("total number of factors are",factor)










   


