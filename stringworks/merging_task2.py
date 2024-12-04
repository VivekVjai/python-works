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

while(i<len1):

    result=result+text1[i]

    i=i+1

while(j<len2):

    result=result+text2[i]

    j=j+1

print(result)


#using for loop 

text1="abcde"

text2="pqr"

result=""

if len(text1)>len(text2):

    for i in range(0,len(text2)):

        result+=text1[i]+text2[i]

balance_text=text1[len(text2):]

result+=balance_text


if len(text2)>len(text1):

    for i in range(0,len(text1)):

        result+=text1[i]+text2[i]

balance_text=text2[len(text1):]

result+=balance_text

print(result)




