arr1=[10,13,8,11,20]

arr2=[2,20,8,7,13]

#common elements without usng in

for i in range(0,len(arr1)):

    for j in range(0,len(arr2)):

        if arr1[i]==arr2[j]:

            print(arr1[i])