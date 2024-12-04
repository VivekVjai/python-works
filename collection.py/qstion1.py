arr=[100,200,300,400,500]

k=2

for k in range(0,k):

    popped_element=arr.pop()

    arr.insert(0,popped_element)

print(arr)