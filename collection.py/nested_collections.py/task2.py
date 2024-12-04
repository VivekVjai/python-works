#user oru index koduthal aa indexilae studentintae avg mark

student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,38,35],
    "anvin":[32,30,40],

}

index=5

for i,elements in enumerate(student_data):

    if i+1==index:   #ividae i start cheyyunathu 0 il ninnnu aanu so i+1
        
        print(elements)  # index same aay vanna elementinae print aakum
           
        marks=student_data.get(elements)  #aa elementilae lsit values edukkan .get("name") koduthu

        avg=sum(marks)//len(marks)

        print(avg)

#list comprehension 

std_avg_marks={k:sum(v)//len(v) for k,v in student_data.items()}

print(std_avg_marks)