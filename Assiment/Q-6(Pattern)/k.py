def patternK():
    n=int(input("Enter number of row:"))
    for i in range(1,2*n):
        for j in range(1,2*n):
            a=i
            b=j
            if(i>n):
                a=2*n-i
            if(j>n):
                b=2*n-j    
            if(a+b==n+1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
patternK()       