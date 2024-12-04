arr=[2,3,4,5,6,7,8,9]

left=0

right=len(arr)-1

sum=7

while(left<right):

    curr_sum=arr[left]+arr[right]

    if curr_sum==sum:

        print(arr[left],arr[right]) #oru pair mathy nkil next lineil break kodukkuka 
        
        left=left+1  #ividae oru pair check cheythittu left incremint cheyyum thazhae right decrementum cheyyum 

        right=right-1

    elif curr_sum<sum:

        left=left+1

    elif curr_sum>sum:

        right=right-1





    