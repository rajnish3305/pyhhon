n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
def multiply(n,m):
    sum=0
    for i in range(1,n+1):
        sum+=m
    return sum        
x=multiply(n,m)
print(x)    