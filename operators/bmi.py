#body mass index 

#bmi= weight in kg/(height in meter)2

weight_in_kg=int(input("enter wight in kg: "))

height_in_cm=int(input("enter height in cm: "))

height_in_meter=height_in_cm/100

bmi=weight_in_kg/(height_in_meter)**2

bmi=round(bmi)

print(bmi)

if bmi<19:

    print("under weight")

elif bmi<25:

    print("normal weight")

elif bmi<30:

    print("over weight")

elif bmi>=30:

    print("obese")

