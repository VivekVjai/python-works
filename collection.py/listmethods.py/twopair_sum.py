arr=[2,3,4,5]


for i in range(0,len(arr)-1):

    for j in range(i+1,len(arr)):

        sum=arr[i]+arr[j]

        if sum==7:

            print(arr[i],arr[j])

            break



#randu alternate numbers ntae sum=7 verunna pairs nae print cheyyan