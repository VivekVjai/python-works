text="ABBACB"

character_count={}

for ch in text:

    if ch in character_count:

        character_count[ch]+=1


    elif ch not in character_count:

        character_count[ch]=1

    if character_count[ch]==2:

        print("first recurssive character is" ,ch)
        break

    

    
