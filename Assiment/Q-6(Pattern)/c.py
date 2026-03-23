def patternC():
    n=int(input("Enter number of row: "))
    for i in range(1,n+1):
        for j in range(n+1-i,0,-1):
            print(j,end=" ")
        print() 
patternC()           
        