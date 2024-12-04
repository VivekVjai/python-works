from re import finditer

f=open("C:\\Users\\user\\Desktop\\pythonworks\\regularexp_fileworks.py\\socialblog.txt")

for line in f: 

    words=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,words)

    for obj in matcher:

        print(obj.group())