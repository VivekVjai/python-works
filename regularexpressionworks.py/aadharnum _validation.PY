from re import fullmatch  

user_input=input("enter the aadhar number  ")

pattern="[2-9{1}[0-9]{11}" 

matcher=fullmatch(pattern,user_input) 

if matcher==None:

    print("invalid")

else:

    print("valid")