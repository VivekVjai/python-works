#3 alphabet
#PCAFHT 4th place alphabet 
#1 alphabet
#4 digit
#1 alphabet


from re import fullmatch  

user_input=input("enter the pancard number  ")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}" 

matcher=fullmatch(pattern,user_input) 

if matcher==None:

    print("invalid")

else:

    print("valid")