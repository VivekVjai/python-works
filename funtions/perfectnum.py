def perfect_num(number):

    num=number

    sum=0

    for i in range(1,number):

        if number%i==0:

            print(i)
        
            sum=i+sum

    print("sum=",sum)

    if sum==num:

        print("is perfect")

    else:

        ("not perfect")


perfect_num(28)
    
