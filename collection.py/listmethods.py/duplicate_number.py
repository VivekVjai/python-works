arr=[1,2,1,2,3,4,3]

arr.sort()

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result==0:

        print(arr[i])
            
        