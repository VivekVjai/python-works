#employee
#id,name,age,salary,department

class Employee:

    id:int
    name:str
    age:int
    departrment:str

     #intialise attributes of employee class(instance variables)
     #instance variablesnae intialise cheyyuka ennullathu constructorntae duty aanu
    def set_employee(self,id,name,age,department): #set_employee kodutheykunnathu athinulilae attributesnae intialise cheyyan vendittanu
        
        self.id=id
        self.name=name
        self.age=age
        self.departrment=department

    def display_emp(self):

        print(self.id,self.name,self.age)

#referance_name=classname()

emp_instance=Employee()

emp_instance.set_employee(100,"vyshnav",24,"hr")

emp_instance.display_emp()

#student[id,name,course]
#set_student()
#display_student()

class Student:
    name:str
    rolnum:int
    age:int
    course:str

    def set_student(self,name,rolnum,age,course):

        self.name=name
        self.rolnum=rolnum
        self.age=age
        self.course=course

    def display_student(self):

        print(self.name,self.age,self.rolnum,self.course)

student_instance1=Student()

student_instance2=Student()

student_instance1.set_student("vyshnav",24,100,"django")

student_instance2.set_student("aadarsh",22,125,"java")

student_instance1.display_student()

student_instance2.display_student()