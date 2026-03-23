n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
def coPrime(n,m):
    a=0
    if(n>m):
        a=m
    else:
        a=n
    for i in range(2,a+1):
        if(n%i==0 and m%i==0):
            return False
        else:
            return True   
x=coPrime(n,m)
print(x)    