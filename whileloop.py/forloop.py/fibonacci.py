
num=int(input("enter the number "))

prev=0

current=1

print(prev)

print(current)

for i in range(1,num-1,):   #n-1 koduthathintae karanam 0 and 1 alread print aay
                          #7 aanu koduthathenkil ini 5 ennam koody print aaya mathy 
                          #so 5 print akan 6 range kodukunnu thatis n-1
    
     next=prev+current

     print(next)

     prev=current    #ee stepilum thottuthazhatha stepilum value swapping aanu cheyunnathu

     current=next






