
from json import load

f=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\employee.json")

data=load(f)

for emp in data:

    print(emp)