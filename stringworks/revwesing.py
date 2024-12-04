#reversing inbetween

text="hellopython"

limit=text.index("o")

reversed=""

for i in range(limit-1,-1,-1):

    reversed+=text[i]

remaining=text[limit:]

print(reversed+remaining)