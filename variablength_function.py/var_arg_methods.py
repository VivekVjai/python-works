def add_numbers(*args):  #  * --> kodutha karanam ethra number of arguments venam nkilum kodukkam 
    
    return sum(args)

print(add_numbers(2,3,4))

print(add_numbers(5,9,30,5))

print(add_numbers(7,8,9,10,11,12))

#crete a function that accept any number of arguments and return the second largest number 

def second_largest(*args):

    sorted_num=sorted(args,reverse=True)

    return sorted_num[1]

print(second_largest(3,6,5,7,8,3))

#  *args--> any number of arguments --> ithu tuple aayittayirikkum receive cheyyunnath

#  **kwargs--> keyword arguments --> ithu dictionary aayittayirikkum receive cheyyunnath

def display_mobile_data(**kwargs):

    print(kwargs.get("name"))

    print(kwargs.get("price"))

display_mobile_data(name="oneplus",price=32000,display="amoled")

#calculator(10,20,30,operation="+")

def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":
    
       return sum(args)
    
    if kwargs.get("operation")=="*":

        result=1

        for num in args:

            result=result*num

        return result
    

print(calculator(3,4,5,6,operation="*"))

print(calculator(3,4,5,6,operation="+"))

#next program


def student_info(*args,**kwargs):

    if kwargs.get("operation")=="avg":

        result=sum(args)/len(args)

        return result
    
    if kwargs.get("operation")=="total":

        return sum(args)
    
print(student_info(35,45,40,50,operation="avg"))


#next program

def sort_numbers(*args,**kwargs):

    if kwargs.get("reverse")=="True":

        return sorted(args,reverse=True)
    
    if kwargs.get("reverse")=="Flase":

        return sorted(args,reverse=False)
    

print(sort_numbers(10,9,8,12,14,5,3,13,reverse="True"))



