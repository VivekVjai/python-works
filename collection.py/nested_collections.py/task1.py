lst=[
    1,2,
     [10,20],
     [1,2,5,[10,3]],
     100
     ]

#ithilae list elements nae mathram edukkanam

list_object=[]

for items in lst:

    if isinstance(items,list):  #isinstance() -->nammal kodukunna item oru certain object aano allyo ennu thirichu ariyan 

        list_object.append(items)

print(list_object)


#list comprehension methods 

list_objects=[item for item in lst if isinstance(item,list)]

print(list_objects)

print(max(list_objects,key=len))   #maximum objects ulla listinae print cheyyan

