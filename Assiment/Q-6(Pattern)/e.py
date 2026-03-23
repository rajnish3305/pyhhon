def patternE():
    n=int(input("Enter number of row: "))
    for i in range(1,n+1):
        for k in range(1,i):
            print(" ",end=" ") 
        for j in range(i,n+1):
            print(j,end=" ")   
        print()    
patternE()    