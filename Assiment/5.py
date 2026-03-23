n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
def hcf(n,m):
    a=0
    b=0
    if(n>m):
        a=m
    else:
        a=n
    for i in range(1,a+1):
        if(n%i==0 and m%i==0):
            b=i
    return b                
y=hcf(n,m)
print("Greatest common divisior is",y)