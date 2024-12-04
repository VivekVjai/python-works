def armstrong_num(number):

    num=number

    count=len(str(number))

    sum=0

    while(num!=0):

        rem=num%10

        sum=(rem**count)+sum

        num=num//10

    print(sum)

    print("armstrong" if sum==number else "not armstrong")

armstrong_num(153)



    