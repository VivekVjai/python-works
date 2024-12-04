text=["hai","hello","hai","hello","hai"]

word_count={}

for w in text:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1

print(word_count)

#dictionary comprehension 

words=["hai","hello","hai","hello","hai","hello","hai","namaste"]

word_freequency={w:words.count(w) for w in words}

print(word_freequency)

#recurssive words

recurssive_words=[k for k,v in word_freequency.items() if v>1]

print(recurssive_words)

#non recurssive words

non_recurssive_words=[k for k,v in word_freequency.items() if v==1]

print(non_recurssive_words)

#most recurssive words