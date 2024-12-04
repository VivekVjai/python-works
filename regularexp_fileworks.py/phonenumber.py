from re import fullmatch

f=open("C:\\Users\\user\\Desktop\\pythonworks\\regularexp_fileworks.py\\phonenumber.txt")

for line in f:  #9876543210\n

    phone=line.rstrip("\n")  #\n mattan 

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher!=None:

        print(phone)



