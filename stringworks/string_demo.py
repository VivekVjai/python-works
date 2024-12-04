#capitalize

text="hellopython"

print(text.capitalize())

#casefold

text="HELLOpYTHon"

print(text.casefold())

#isalpha

text="hellopython"

print(text.isalpha())

#isdigit

text="hellopython"

print(text.isdigit())

#isalnum

text="hellopython12345"

print(text.isalnum())

#strings le chara oronnai print cheyyan 

text="hellopython12345"

for ch in text:

    print (ch)

text="python java javscript ruby"

words=text.split(" ")

print(words)

#remove \n

text="\t this \t is a line \t"

new_text=text.strip("\t")

print(new_text)  #ividae centerlae remove akilla 

#lstrip  --> left end lae remove akan 

#rstrip ---> right end lae remove akan 

#replace (o--->a)

text="hello world program"

new_text=text.replace("o","a",)

print (new_text)

#replace (o--->a , count)

text="hello world program"

new_text=text.replace("o","a",2) #ividae first 2 'o' mathram replace akum

print (new_text)

#slice 

text="python programming"
    # 012345678901234567
    # string_object[start:end+1:step]

sliced1=text[0:6]

sliced2=text[7:]#end mention cheythilla enkil default aayitt end vera edukkum


print(sliced1)
print(sliced2)

#reverse a string

text=("python programming")

reversed=text[::-1]  #entire string reversed aakum

print(reversed)

#index

text="python"

print(text.index("o"))


#name mathram print cheyyanam

text="vipinkumar@gmail.com"

limit=text.index("@")

print(text[0:limit])

#reversing inbetween

text="hellopython"

limit=text.index("o")

reversed=""

for i in range(limit-1,-1,-1):

    reversed+=text[i]

remaining=text[limit:]

print(reversed+remaining)





























