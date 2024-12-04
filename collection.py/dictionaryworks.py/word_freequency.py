text="ABABBACDBCEFE"

character_freequency={ch:text.count(ch) for ch in text}

print(character_freequency)

#print non recursive elements

for k,v in character_freequency.items():

    if v==1:

        print(k)


#dictionary comprehension

nonrecurssive_chara=[k for k,v in character_freequency.items() if v==1]

print(nonrecurssive_chara)