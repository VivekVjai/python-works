from re import fullmatch

date=input("enter the date ")

pattern=("0?[1-9]|[12][0-9]|3[01]")

#0? vannalum illenkilum 1-9--> valid #[12][0-9] 1or2 vannal 0-9--> valid

matcher=fullmatch(pattern,date)

if matcher==None:

    print("invalid")

else:

    print("valid")