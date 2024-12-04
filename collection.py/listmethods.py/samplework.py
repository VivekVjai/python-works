

lst=[3,6,7]

for i in range(0,len(lst)-1):

    for j in range(i+1,len(lst)):

        sum=lst[i]+lst[j]

        if sum==9:

            print(lst[i],lst[j])

        if sum==13:

            print(lst[i],lst[j])

        if sum==10:

            print(lst[i],lst[j])

