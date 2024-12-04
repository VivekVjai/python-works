def palindrome(number):

    num=number

    rev=0

    while(num!=0):

        div=num%10

        rev=rev*10+div

        num=num//10

    print(rev)

    print("palindrome " if number==rev else "not palindrome ")

palindrome(133431)