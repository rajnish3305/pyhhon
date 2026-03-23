def perfect():
    n=int(input("Enter number : "))
    a=0
    for i in range(1,n):
        if n%i==0:
         a=a+i
    if a==n:
        print(n,"is a perfect number")  
    else:
        print(n,"is not a perfect number") 
 
perfect()                  