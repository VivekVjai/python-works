arr=[10,10,20,30,40,50,40]

#output=10,20,30,40

st=set() #oru empty set create cheyunnu

for num in arr:

    st.add(num)  #empty set lekku arr le oro num nae add cheyunnu 

print(st)  #duplicates allowed alla insertion order prevent cheyunnilla 

#intersection() --->method

st1={10,20,30,40,50}

st2={30,40,50,60,70}

intersection_set=st1.intersection(st2)

print(intersection_set)

#union()---> method

union_set=st1.union(st2)

print(union_set)

#difference()---->method

difference_set=st1.difference(st2)

print(difference_set)

#issubset()

set1={10,20,30}

set2={10,20,30,40,50,60}

print(set1.issubset(set2))

print(set2.issuperset(set1))

#symmetric differece

set_1={1,2,3,10,20}

set_2={1,2,3,4,5}

syymetric_difference=set_1.symmetric_difference(set_2)

print(syymetric_difference)

#update()

st1={1,2,3,4,5,6}
st2={5,6,7,8,9}

st1.update(st2)

print(st1)