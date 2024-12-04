years=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\years.txt","r")

leap_year=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\leap_year.txt","w")

century_year=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\century_years.txt","w")

for y in years:

    y=int(y)

    if y%4==0:

        leap_year.write(str(y)+"\n")

    if y%100==0:

        century_year.write(str(y)+"\n")

years.close()

leap_year.close()

century_year.close()