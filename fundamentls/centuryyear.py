#century year

year=int(input("enter the year: "))

is_century_year=year%100==0

print(is_century_year)


#non century year

year=int(input("enter the year: "))

is_non_century_year=year%100!=0

print(is_non_century_year)