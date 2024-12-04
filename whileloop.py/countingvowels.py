#programme to print no of vowels in a string

string=input("enter the statement:  ")

str=string.lower()

numvowels=0

count=0

vowels="a e i o u"

numstr=len(str)

while(count<=numstr):

    if(str[count] in vowels ):
        
        numvowels=numvowels+1

print(numvowels)