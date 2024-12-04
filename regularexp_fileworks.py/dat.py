from re import findall

f=open("C:\\Users\\user\\Desktop\\pythonworks\\regularexp_fileworks.py\\data.txt")

date=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{2}"

all_dates=findall(pattern,date)

for dates in all_dates:

    print(dates)

