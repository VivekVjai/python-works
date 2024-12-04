#elglish le ella alphabets undenkil pangram allenkil not pangram 

text="the quick brown fox jumps over the lazy dog"

alphabets=("abcdefghijklmnopqrstuvwxyz")

is_pangram=True

for ch in alphabets:  #alphabetsil ninnu aanu characters edutath karanam mukalil ninnu eduthal spacem chara aay verum 

    if ch not in text:

        is_pangram=False

        break

print(is_pangram)



        


