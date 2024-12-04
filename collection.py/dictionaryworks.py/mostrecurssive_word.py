text="this is a simple program question this is to find words with maximum nuber of characters in this text"

words=text.split(" ")

def get_count(w):

    return words.count(w)

freequent_word=max(words,key=get_count)

print(freequent_word)

