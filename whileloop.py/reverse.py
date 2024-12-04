#to reverse a number

num=int(input("enter the number to be reversed:  "))  #321===>123  (1, 1*10+2=12, 12*10+3=123  and so on this is the concept)

rev=0 

while(num>0):  #num greater thn zero akunna vera loop work cheyyum

    div=num%10  #given digit ntae last digit obtain cheyyan aanu 10 vech mode cheyunnath

    rev=rev*10+div  #rev=0*10+last number= gives first number 

    num=num//10  #gives the integer to the second loop

print(rev)

 