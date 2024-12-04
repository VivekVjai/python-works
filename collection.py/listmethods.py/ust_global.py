arr=[100,200,300,400,500,600,700,800]

#result=[100,800,300,600,500,400,700,200]

left=1
right=len(arr)-1


while(left<right):


        arr[left],arr[right]=arr[right],arr[left]

        left+=2
        right-=2
        

print(arr)

#aother method

#odd_position_elemets=[arr[i] for i in range(0,len(arr)) if i%2!=0]

#print(odd_position_elemets)

#for i in range(1,len(arr),2):




