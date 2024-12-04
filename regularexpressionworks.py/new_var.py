

#starting with an alphabet from p-t
#in second place mustbe a number that is \by 3
#followed by anynumber alphabet,number,@

from re import fullmatch  

user_input=input("enter variable name ")

pattern="[p-tP-T][369][0-9A-Za-z@]*" 

matcher=fullmatch(pattern,user_input) 

if matcher==None:

    print("invalid")

else:

    print("valid")