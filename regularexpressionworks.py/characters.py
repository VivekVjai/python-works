from re import finditer

text="i have 3 cars,2bikes and 1 cycle"

#pattern="\w"  #[A-Za-z0-9]  alphaneumaric
#pattern="\d"   #[0-9]  digits
#pattern="\D"    #[^0-9]  exclude digits
#pattern="\W"      #[^A-Za-z0-9]  special characters
#pattern="\s"       #spaces
pattern="\S"        #exclude spaces

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())