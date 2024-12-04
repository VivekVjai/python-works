#1800-2024

f=open("C:\\Users\\user\\Desktop\\pythonworks\\database\\years.txt","w")

for year in range(1800,2025):

    f.write(str(year)+"\n")  #str fuction nae mathramae write cheyyan patullu so int year nae str akan str(year)

f.close()