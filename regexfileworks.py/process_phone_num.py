from re import fullmatch

f=open("C:\\Users\\user\\Desktop\\pythonworks\\regexfileworks.py\\process_phone_num.txt")

for line in f:

    phone=line.strip("\n")

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher !=None:

        print(phone)

