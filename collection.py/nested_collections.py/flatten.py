arr=[
    [10,20],
    [20,30],
    [30,40],
    [40,50]

]

result=[]

for lst in arr:  #arr lae listinae itterate cheyyunnu 

    for num in lst:  #lst lae numbersinae itterate cheyunnnu 

        result.append(num)   #itterate cheythu edutha numbersninae oru empty listlekku add cheyunu 

print(result)

#list comprehenssion method

flatten_list=[num for lst in arr for num in lst]

print(flatten_list)