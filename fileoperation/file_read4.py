f=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\question.txt","r")

words=[]

for lines in f:

    lines=lines.rstrip("\n") #oro line nteum endle "\n" na remove aakan 

    all_words=lines.split(" ")  #ini first line lae oro words nae split cheyyanam 

    for w in all_words:

        words.append(w)  #all wordslae oro wordnem append cheyyannam 

print(words)

word_count={w:words.count(w) for w in words}

value_key=[[v,k] for k,v in word_count.items()]

print(sorted(value_key,reverse=True))

