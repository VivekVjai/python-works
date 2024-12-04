#rule
#10 digit 
#validate mobile num 


from re import fullmatch  

user_input=input("enter mobile number ")

pattern="(91)+[0-9]{10}" #(91)? koduthal () koduthathu 91 nae anganae group cheyyan ? koduthathu veram verathayum irikkam (91)+ koduthal 91 koduthillel invalid aakum 

matcher=fullmatch(pattern,user_input) 

if matcher==None:

    print("invalid")

else:

    print("valid")