from re import fullmatch  #fullmatch koduthathinal nammal kodutha patten exact match akanm 

user_input=input("enter variable name ")

#rule
#start with alphabets
#any number alphabets,digits,_

pattern="[a-zA-Z][A-Za-z0-9_]*"  #according to the above rule 

matcher=fullmatch(pattern,user_input)  #pattern exact match ayilla nkil matcherilae default value none ayirikkum 

if matcher==None:

    print("invalid")

else:

    print("valid")