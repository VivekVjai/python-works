#body mass index 

#bmi= weight in kg/(height in meter)2

weight_in_kg=int(input("enter wight in kg: "))

height_in_cm=int(input("enter height in cm: "))

height_in_meter=height_in_cm/100

bmi=weight_in_kg/(height_in_meter)**2

bmi=round(bmi)

print(bmi)

if bmi<19:
    print("""you are under weight
            you should go under a calorie excess diet plan
            to know the calorie you needed to check bmr """)

elif bmi<25:

     print("""you are in normal weight
            you can continue your diet plan and workouts
            to know the calorie you needed to check bmr """)

elif bmi<30:

    print("""you are over weight
            you should go under a calorie deficit diet plan
            to know the calorie you needed to check bmr """)


elif bmi>=30:

    print("""you are obese
            you should go a calorie deficit diet plan immediately
            to know the calorie you needed to check bmr """)


#now calculate the bmr of the person
print("for bmr calculation enter the following details")


age=int(input("enter the age "))

gender=input("enter the gender ").lower()

print(age,weight_in_kg,height_in_cm,gender)

if gender=="male":

    bmr=(10*weight_in_kg+6.25*height_in_cm-5*age+5)

elif gender=="female":

    bmr=(10*weight_in_kg+6.25*height_in_cm-5*age-161)

else:

    print("enter a valid gender")

print(f"your basic metabolic rate is{bmr}")

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

total_calorie_needed=round(calorie*1.2)


print(f"total number of calorie you needed to maintain your weight={total_calorie_needed}")


#weight reduction 

target_weight=int(input("""
                        
            if you want to reduce weight please enter 1
                        
            if you want to increase weight please enter 2 
                        
            if you want to quit this page enter 3 
                                                        """))


if target_weight==1:

    weight_to_reduce=int(input("enter the weight to reduce: "))

    no_days_to_reduce=int(input("enter the no of days you want to reduce the weight within: "))

    daily_calorie_deficit=weight_to_reduce*7700/no_days_to_reduce

    print(f"""your daily calorie goal is {daily_calorie_deficit}
          
          
            yout can rearrange your diet with the following according to the calorie needed

              Non-starchy vegetables: spinach, broccoli, cauliflower, peppers, mushrooms..

              Fish and shellfish: sea bass, salmon, cod, clams, shrimp, sardines, trout, oysters, etc.

              Eggs: whole eggs are more nutrient dense than egg whites

              Poultry and meat: chicken, turkey etc.

              Legumes: chickpeas, kidney beans, lentils, black beans and more

              Healthy fats: avocados, olive oil, unsweetened coconut, avocado oil, etc.

              Dairy products: plain yogurt, kefit, and cheese
          
              and do exercise daily
             
              all the best """)

elif target_weight==2:

    weight_to_increase=int(input("enter the weight to increase: "))

    no_of_days_increase=int(input("enter the no days you want to gain the weight within: "))

    daily_calorie_excess=weight_to_increase*7700/no_of_days_increase

    print(f"""your daily calorie goal is {daily_calorie_excess} 
          
              you can add high-calorie foods in your diet such as:

              Butter, honey, and brown sugar, added to foods to make them taste better.

              Oils, sauces, and gravies.

              Peanut butter.

              Whole milk, yogurt, mayonnaise, and sour cream.

              Granola cereal with fruit and granola bars.

              Muffins, pancakes, waffles, and other breads.

              Milkshakes, puddings, and custard
          
              all the best""")
else:

    print("*****thank you*****")














