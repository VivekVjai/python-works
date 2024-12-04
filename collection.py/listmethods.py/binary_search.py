arr=[1,2,3,4,5,6,7,8,9]

arr.sort()

search_element=int(input("enter the search element  "))

is_present=False

lower=0

upper=len(arr)-1

while(lower<=upper):

    mid=(lower+upper)//2

    if search_element==arr[mid]:

        is_present=True

        break

    elif search_element<arr[mid]:

        upper=mid-1

    elif search_element>arr[mid]:

        lower=mid+1

print(is_present)



    