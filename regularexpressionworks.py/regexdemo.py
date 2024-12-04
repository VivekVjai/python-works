from re import finditer

text="abababababab"
     #0123456789
matcher=finditer("ab",text)  #[object  (start,group)]
                             #[(0,ab)]


for m in matcher:

    print(m.start(),m.group())


from re import finditer

text="fatcatrunsveryfasttocaththerat"

object=finditer("at",text)

for obj in object:

    print(obj.start(),obj.group())


