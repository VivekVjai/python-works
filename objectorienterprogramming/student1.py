#costructor 

#initialising instance variables

#python-->__init__

#java--> classname

#javscript--> constrcutor

#ella languagelum costructorntae function initialisning instance variables aanu


class Student:
    name:str
    rolnum:int
    age:int
    course:str

    def __init__(self,name,rolnum,age,course):

        self.name=name
        self.rolnum=rolnum
        self.age=age
        self.course=course

    def display_student(self):

        print(self.name,self.age,self.rolnum,self.course)

student_instance1=Student("vivek",29,125,"pythondjango")  #constructor koduthal pinnae object create cheyyumbol constroctorinae call cheyyanda karyam illa 
4
student_instance1.display()