#to print the list of squares of the numbers in the list

arr=[2,3,4,5,6,7]

square=[]

for num in arr:

    sq=num**2

    square.append(sq)

print(square)


#to print list of cubes

arr=[2,3,4,5,6,7]

cubes=[]

for num in arr:

    cubes.append(num**3)

print(cubes)


#list comprehesion

#reference=[return  loop   condition]

#cubes

cubes=[num**3  for num in arr]

print(cubes)

#add five

add_five=[num+5 for num in arr]

print(add_five)

#filter

even_num=[num for num in arr if num%2==0]

print(even_num)

#return a new list if num+1 if num>5 else num-1

arr=[2,3,4,5,6,7]

mapped_num=[num+1 if num>5 else num-1 for num in arr]

print(mapped_num)

#vowel words

text=["apple","iphone","orange","potato"]

vowel_words=[w for w in text if w[0] in ["a","e","i","o","u"]]

print(vowel_words)

#consonent_word

consonent_word=[w for w in text if w[0] not in ["a","e","i","o","u"]]

print(consonent_word)

#longest_word

long=max([len(w) for w in text])

longest_word=[w for w in text if len(w)==long]

print(longest_word)

