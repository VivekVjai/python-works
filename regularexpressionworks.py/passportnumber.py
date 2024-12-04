from re import fullmatch  

user_input=input("enter the passport number  ")

pattern="[A-Z]{1}[1-9]{1}[0-9]{1}[0-9]{4}[1-9]{1}" 

matcher=fullmatch(pattern,user_input) 

if matcher==None:

    print("invalid")

else:

    print("valid")