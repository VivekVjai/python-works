#validate month 01-12

from re import fullmatch

month=input("enter the month ")

pattern="([1-9]|0[1-9]|1[0-2])" #1 to 9 start cheyyam or(|) 0 il start cheythal 1 to 9 vera veram or 1 il start cheythal 0 to 2 vera veram 

matcher=fullmatch(pattern,month)

if matcher==None:

    print("invalid")

else:

    print("valid")