def patternI():
    n=int(input("Enter number of row:"))
    for i in range(1,n+1):
        for j in range(1,2*n):
            a=i
            b=j
            if(j>n):
                b=2*n-j
            if(a==1 or a==b):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()     
patternI()                   