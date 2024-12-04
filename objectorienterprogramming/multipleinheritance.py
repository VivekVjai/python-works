class Person:

    name:str
    age:int

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def display_person_info(self):

        print(self.name,self.age)

class Employee:

    emp_id:int
    salary:int

    def __init__(self,emp_id,salary):

        self.emp_id=emp_id
        self.salary=salary

    def display_employee_info(self):

        print(self.emp_id,self.salary)

class Manager(Person,Employee):

    department:str

    def __init__(self,age,name,emp_id,salary,department):

        Person.__init__(self,age,name)

        Employee.__init__(self,emp_id,salary)

        self.department=department

    def display_manager_info(self):

        self.display_person_info()

        self.display_employee_info()

        print(self.department)

manager_instance=Manager("hai",32,10411,52000,"human resource")

manager_instance.display_manager_info()


#next program 

class Cusine:
    
    name:str

    def __init__(self,name):
        
        self.name=name

    def display_cusine(self):

        print(self.name)

class Meal_type:

    meal:str

    def __init__(self,meal):

        self.meal=meal

    def display_meal(self):

        print(self.meal)

class Dish(Cusine,Meal_type):

    dish:str

    def __init__(self,name,mealtype,dish):

        Cusine.__init__(self,name)

        Meal_type.__init__(self,mealtype)

        self.dish=dish

    def display_dish(self):

        self.display_cusine()

        self.display_meal()

        print(self.dish)

dish_instance=Dish("italian ","pasta ","breakfast")

dish_instance.display_dish()