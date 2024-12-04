from re import fullmatch  

user_input=input("enter the driving licence number  ")

pattern="[A-Z]{2}[ -]?[0-9]{2}[ -]?[0-9]{4}[ -]?[0-9]{7}" 

matcher=fullmatch(pattern,user_input) 

if matcher==None:

    print("invalid")

else:

    print("valid")