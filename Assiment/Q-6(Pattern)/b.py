def patternB():
    n=int(input("Enter number of row: "))
    for i in range(1,n+1):
        for j in range(1,n+1-i):
            print(" ",end=" ")
        for k in range(i,0,-1):
            print(k,end=" ")
        for q in range(2,i+1):
            print(q,end=" ")
        print() 
patternB()                   