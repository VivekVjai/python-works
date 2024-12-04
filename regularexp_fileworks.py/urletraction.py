from re import findall

f=open("C:\\Users\\user\\Desktop\\pythonworks\\regularexp_fileworks.py\\urlextraction.txt")

content=f.read() #loop use cheyyanda read use cheythal f lae conent full ippol connent enna variablel vannatund 

pattern=("https?://[\w\S./]+")  #ithil  s?--> s mathram optional aaittu eduthu

urls=findall(pattern,content)

for url in urls:

    print(url)