#lambda functions

def add_number(num1,num2):

    return num1+num2


print(add_number(100,200))

#adding two numbers using lambda function

add=lambda num1,num2:num1+num2

print(add(100,300))

#substracting two numbers using lambda function

sub=lambda num1,num2:num1-num2

print(sub(200,100))

#cubes using lambda 

cubes=lambda num:num**3

print(cubes(8))

#max two of two string using lambda 

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_two("vivek","revathy"))

#min two of two strings 

min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2

print(min_two("vivek","revathy"))

#smart sub  substract from the largest

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(8,16))

#longest string

words=["hello","hai","morning","test"]

def get_length(word):

    return len(word)

print(max(words,key=get_length))

#using lambda 

get_length=lambda word:len(word)

print(max(words,key=get_length))

print(min(words,key=get_length))

#sorting the words

text="this is a simple program question to find words with maximum nuber of characters"

#step1 split text to words

words=text.split(" ")

def get_length(w):

    return len(w)

srt_words=sorted(words,key=get_length,reverse=True)

print(srt_words)


#using lambda

text="this is a simple program question to find words with maximum nuber of characters"

words=text.split(" ")

get_length=lambda word:len(word)

srt_words=sorted(words,key=get_length)

print(srt_words)



