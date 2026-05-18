# Case Study 6:
#  Write a menu-driven program using functions:
# Menu:
# 1. Find Square
# 2. Find Cube
# 3. Exit
# •	Take user choice.
# •	Perform operation using separate functions.
# •	Use loop for menu repetition.

while 1>0:
    print("Menu:")
    print("1-->Suare")
    print("2-->Cube")
    print("3-->Exit")
    
    choice = int(input("Enter Opertion number: "))
    if choice ==1:
        def square():
            a = int(input("Enter Number to get Square: "))
            print(f"Square of {a} is {a**2}")
        square()
    elif choice ==2:
        def Cube():
            a = int(input("Enter Number to get Cube: "))
            print(f"Cube of {a} is {a**3}")
        Cube()    
    else:
        print("Exit")
        break                
        
