f_words=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\words.txt")

palindrome=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\palindrome.txt","w")

for w in f_words:

    w=w.rstrip("\n")

    reversed_word=w[::-1]

    if w==reversed_word:

        palindrome.write(w+"\n")

f_words.close()

palindrome.close()

