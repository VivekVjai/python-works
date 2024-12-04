from re import finditer

text="abbbaabbabaababbbbaaaab"

#pattern="a{2}"  #a yudae quantiy 2 ennam venam ennu
#pattern="a{1,3}"  #a min 1 maximum 3 --> {} limit und 
pattern="a*"    # * means any number including zero athayathu ethra ennam venam enkilm veram 

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())