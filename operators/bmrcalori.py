age=int(input("enter the age "))

weight=int(input("enter the weight "))

height=int(input("enter the height in cm "))

gender=input("enter the gender ").lower()


print(age,weight,height,gender)

if gender=="male":

    bmr=(10*weight+6.25*height-5*age+5)

elif gender=="female":

    bmr=(10*weight+6.25*height-5*age-161)

else:

    print("enter a valid gender")

print(bmr)

activity_level=int(input("""
     select activity levels
                   
press 1 for sedentary
press 2 for lightly active
press 3 for moderate active 
press 4 for very active
press 5 for extreme active

"""))

if activity_level==1:

    calorie=bmr*1.2

elif activity_level==2:

    calorie=bmr*1.375

elif activity_level==3:

    calorie=bmr*1.55

elif activity_level==4:

    calorie=bmr*1.725

elif activity_level==5:

    calorie=bmr*1.9

else:
    
    ("******print a valid data*******")

total_calorie_needed=calorie*1.2


print(f"total number of calorie you needed to maintain your weight={total_calorie_needed}")


