#create dictionary employee with keys eid, name , salary ,department, experience 

employee={"eid":1245,"name":"manoj","salary":25000,"department":"hr","experience":2}

#add contact

employee["contact"]=9854633656

print(employee)

#if experience >5 update salary as current_salary+10000
#else salary as current _salary +5000

if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

print(employee)

#add role as sde if exp>5 else add role as jde 

if employee["experience"]>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"

print(employee)