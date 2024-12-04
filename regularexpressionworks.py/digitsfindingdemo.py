#from re import finditer

#text="i have 3 cars,2bikes and 1 cycle"

#pattern="[a-zA-Z]"  #[a-z] chk for all lowercase alphabets, [a-zA-Z]check for alL alphabets

#matcher=finditer(pattern,text)

#for obj in matcher:

    #print(obj.start(),obj.group())



#from re import finditer

#text="i have 3 cars,2bikes and 1 cycle"

#digits="[0-9]"

#match=finditer(digits,text)

#for dg in match:

 #   print(dg.start(),dg.group())


#from re import finditer

#text="i have 3 cars,2bikes and 1 cycle"

#digits="[a-zA-Z0-9]"  #alpha neumeric check cheyyum 

#match=finditer(digits,text)

#for dg in match:

 #   print(dg.start(),dg.group())




from re import finditer

text="i have 3 cars,2bikes and 1-cycle"

#pattern="[^ak]"  #inganae koduthal artham excluding a or k baki ellam print aakum 

#match=finditer(pattern,text)

#for dg in match:

 #   print(dg.start(),dg.group())

#all lower case alphabets exclude a,k

#pattern="[^akA-Z0-9,\- ]"  #ak,capital a to z,0 to 9,\-  -->  ' - ',  space ithrayum exclude aakum 

pattern="[^a-zA-Z0-9]"  #special charctersinae mathram print aakan like space highphen coma etc 

match=finditer(pattern,text)

for dg in match:

    print(dg.start(),dg.group())


#pattern="[a-zA-Z]"  #[a-z] chk for all lowercase alphabets, [a-zA-Z]check for alL alphabets

#digits="[0-9]"  #digitsnae mathram print 

#digits="[a-zA-Z0-9]"  #alpha neumeric check cheyyum

#pattern="[^ak]"  #inganae koduthal artham excluding a or k baki ellam print aakum 

#pattern="[^akA-Z0-9,\- ]"  #ak,capital a to z,0 to 9,\-  -->  ' - ',  space ithrayum exclude aakum 

#pattern="[^a-zA-Z0-9]"  #special charctersinae mathram print aakan like space highphen coma etc 

# ^ --->  cap symbol