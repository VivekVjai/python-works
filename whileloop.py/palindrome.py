#palindfrome check (palindrome num is a number that remains the same when it is reversed eg 121,1234321,)

num=int(input("enter the number to be checked: "))

number=num

rev=0

while(num>0):

    div=num%10

    rev=rev*10+div

    num=num//10

print(rev)

if (rev==number):

    print("the entered number is palindrome")

else:

    print ("the entered number is not palindrome")