arr=[10,20,30,40,2,3]

arr_dictionary={}

for i in arr:

    arr_dictionary[i]=i*i

print(arr_dictionary)

#dictionary comprehension

#syntax ==>  {key:values  iteration   condition}

#q: to print cubes of the above seq in dictionary

result={num:num**3 for num in arr}

print(result)

#even numbers squares and odd numbers cubes in two different dictionaries 

even_sqaures={num:num**2 for num in arr if num%2==0}

odd_cubes={num:num**3 for num in arr if num%2!=0}

print(even_sqaures)

print(odd_cubes)

#freequency of numbers

pqr=[10,20,30,40,2,3,7,8,9,10,30]

freequency_count={num:pqr.count(num) for num in pqr}

print(freequency_count)