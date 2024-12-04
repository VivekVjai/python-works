st=set()  #class--> set

st={10,20,30}  #class-->set

st={}   #class-->dictionary

st={10,20,30,10,20,30,"hello","hai",True}

print(st)

colours={"red","green","blue"}

colours.add("yellow")

print(colours)

colours=["red","green","blue"]

colours_set=set(colours)

print(colours_set)

#sample question

text1="this is a test to remove duplicate words this test is simple"

text2="this simple test remove duplicate words"

#split text

words1=text1.split(" ")

words2=text2.split(" ")

print(set(words2).issubset(set(words1))) 