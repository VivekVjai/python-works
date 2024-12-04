from re import fullmatch

gmail=input("enter the gmailid ")

pattern="([a-z]+[a-z0-9]{5,63}@gmail.com"
#[a-z]+ inganae koduthal atoz min orennam nkilm venam 

matcher=fullmatch(pattern,gmail)

print("invalid" if matcher==None else "valid")