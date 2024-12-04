num1=int(input("enter the first number "))

num2=int(input("enter the second number "))

number1=num1

number2=num2

n=2

if(number1>number2):

     div=number1%number2

     if (div==0):

        print("lcm = ",number1)


     else:

          while(div==0): 
            
           num1=number1*n
           
           div=num1%num2
               
           n=n+1

     print("lcm= " ,num1)


elif(number2>number1):
        
        div=number2%number1

        if(div==0):
             
             print("lcm= ", number2)     
             
             
        else:
          
          while(div==0):
               
               num2=number2*n
               
               div=num2%num1
               
               n=n+1

        print("lcm= " ,num2)


        

        





