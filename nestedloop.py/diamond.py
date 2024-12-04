for row in range(1,7,):
    
    for space in range(1,7-row):
          
          print(" ",end="")

    for colum in range(1,row+1):
           
           print("* ",end="")

    
    print()

for row in range(1,7):

    for space in range(row,1,-1):
          
          print(" ",end="")

    for colum in range(7-row,0,-1):
           
           print("* ",end="")

    print()

