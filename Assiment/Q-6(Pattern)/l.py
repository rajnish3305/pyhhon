def patternL():
    n=int(input("Enter number of row:"))
    nos=1
    nog=n-1
    for i in range(1,2*n):
        for k in range(1,nog+1):
            print(" ",end=" ")
        for j in range(1,nos+1):
            print("*",end=" ")
        if(i<n):
            nos=nos+2
            nog=nog-1
        else:
            nos=nos-2
            nog=nog+1            
        print()   
patternL()    