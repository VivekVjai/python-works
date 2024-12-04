#starting with KL
#2DIGIT
#alpha min 1 max2 
#4 digit 

from re import fullmatch  

user_input=input("enter vehicle regstration number  ")

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}" 

matcher=fullmatch(pattern,user_input) 

if matcher==None:

    print("invalid")

else:

    print("valid")