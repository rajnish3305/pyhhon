def patternM():
    n=int(input("Enter numbe rof row:"))
    for i in range(1,n+1):
        for k in range(1,i):
            print(" ",end=" ")
        for j in range(1,n+2-i):
            print("$",end=" ")
        print()  
patternM()      