text=input("enter the text ")

length=len(text)-1

reversed_str=""

for i in range(length,-1,-1):  #detailed notebookil und

    reversed_str+=text[i]

print(reversed_str)