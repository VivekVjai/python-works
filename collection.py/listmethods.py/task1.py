arr1=[1,2,3,5]

n=1

for i in range(0,len(arr1)):
        
        
        if n==arr1[i]:
              
            n=n+1

        else:
              
              break
        
print(n)

#or

arr1=[1,2,3,5]

i=0
j=1

while(i<len(arr1)):
      
      if arr1[j]-arr1[i]==1:
            
            i+=1

            j+=1
            
      else:
            
            break
      
print(arr1[i]+1, "is missing")



        
