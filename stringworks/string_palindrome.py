text=input("enter the text ")

reversed_text=text[::-1]

if reversed_text==text:

    print("palindrome")

else:

    print("not palindrome ")


#combined

text=input("enter the text ")

reversed_text=text[::-1]

print ("palindrome"if reversed_text==text else "not palindrome")