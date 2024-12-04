text1="pqrs"

text2="abcd"

len1=len(text1)
len2=len(text2)

i=j=0

result=""

while(i<len1 and j<len2):

    result=result+text1[i]+text2[j]

    i=i+1
    j=j+1


print(result)

#using "for loop" this is the simple method.......


text1="abc"

text2="pqr"

result=""

for i in range(0,len(text1)): #length of text1 and text2 are equal in this case 

    result+=text1[i]+text2[i]

print(result)

    

