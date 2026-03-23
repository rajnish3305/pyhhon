n=int(input("Enter Day number : "))
if(n>7):
    print("Not valid day number")
elif(n<6):
    print("Working day")
    if(n==1):
        print("Monday") 
    elif(n==2):
        print("Tuesday")
    elif(n==3):
        print("Wednesday")
    elif(n==4):
        print("Thrusday") 
    else:
        print("Friday")
else:
    print("Week End")
    if(n==6):
        print("Saturday")
    else:
        print("Sunday")                              