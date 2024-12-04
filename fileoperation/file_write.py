 

f=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\names.txt","w")

text="hello world"

f.write(text)

f.close()

#another program

f=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\names.txt","w")

languages=["python","java","c#","javascript"]

for l in languages:

    f.write(l + "\n")  #"\n" koduthathu kond oro languages print aaya sheshavum next line lekku pokum 

f.close()