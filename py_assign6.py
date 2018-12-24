# Creating a playboard

x=int(input("Enter the number of rows and columns (it should be odd): "))

def PlayBoard(x):

 if(x>209):
  print("Max. value 209 exceeded !")	
  return False	

 else:

  for row in range(1,x+1):
  
    if row%2==1:
    
     for column in range(1,x+1):

        if column%2==1:

          if column!=x:
           print(" ",end="")

          else:
           print(" ")  

        else:
         print("|",end="")  

    else:  
     print("-"*x)    

  return True


PlayBoard(x)