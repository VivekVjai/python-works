#dictionary methods

#employee id,name,department,age,salary

employee={"id":112,"name":"sachin","deparment":"it","age":34,"salary":35000}

print(employee)

#get---> method

print(employee.get("salary"))

#pop-->method

employee.pop("salary")

print(employee)

#return all keys ==> .keys()

for k in employee.keys():

    print(k)

#fetch all values ==> .values()

for v in employee.values():

    print(v)
    
#fetch key and values==> .items()

for k,v in employee.items():

    print(k,v)