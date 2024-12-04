f=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\fruits.txt","r")

fruits=[]  #fruits nae oru listil print cheyyanam so fruits ennoru empty list create cheyyanam 

for line in f:

    fruits.append(line)  #empty list lottu append cehyunu 

print(fruits)  #ithinae print cheyumbol listil ellam "\n" verum 

#"\n" nae remove aakan ---> .rstrip()

f=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\fruits.txt","r")

fruits=[]  

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)