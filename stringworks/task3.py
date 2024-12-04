#print first recussive charachter "a"

text="abcabc"

for i in range(0,3,3):

    result=text[i]

    print(result)


#another method

text="abcabc"

for ch in text:

    if ch==ch:

        print(ch)

        break