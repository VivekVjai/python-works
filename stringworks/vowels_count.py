text="hellopython"

for ch in text:

    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":

        print (ch)


#another method

text="hellopython"

vowels="aeiou"

for ch in vowels:

    if (ch in text)==(ch in vowels):

        print(ch)
