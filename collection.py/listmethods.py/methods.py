# .append()

colours=["red","greee","blue"]

colours.append("yellow")   #.append() -- new objectinae listintae endilekku add cheyyan aanu use cheyunnathu

print(colours)

# .pop()   ---> remove te last object and returns it

popped_element=colours.pop()

print(colours)

print(popped_element)

colours.pop(1)

print(colours)

# .inset(index,object)

colours.insert(0,"purple")

print(colours)

# .index(object)  --> its returns the first index of the object we given if its in the list

red_index=colours.index("red")

print(red_index)

#copy() --> oru list ntae copy list create cheyyan vendittut

abc_fav_colours=["red","green","blue","black"]

cde_fav_colours=abc_fav_colours.copy() # copy use cheyyathae equalto matram aanu use chyeyyunath nkil pop cheyumbol athu abc coloursinem badhikkkum

cde_fav_colours.pop()

print("abc fav",abc_fav_colours)

print("cde fav",cde_fav_colours)

#sorting

lst=[2,5,6,3,4,6]

lst.sort() #---> by default ascending order il sort aakum 

print(lst)

lst.sort(reverse=True)  #--> descending orderil sort cheyyan 

print(lst)

#extend

fruits=["apple","orange","mango"]

products=["onion","potato","brinjal"]

products.extend(fruits)

print(products)

#reverse

#to reverse

#count

lst=[10,20,30,40]

ten_occurance=lst.count(10)

print(ten_occurance)