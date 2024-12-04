text="ABAABCAABC"

def get_count(ch):

    return text.count(ch)
    
most_freequent_chara=max(text,key=get_count)

print(most_freequent_chara)

least_freequent_char=min(text,key=get_count)

print(least_freequent_char)


