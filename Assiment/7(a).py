import math
n=int(input("Enter value of n:"))
x=int(input("Enter value of x:"))
def sumOfSeries(n,x):
    operation=1
    sum=0
    for i in range(0,n+1,2):
        term=(x**i)/math.factorial(i)
        sum+=operation*term
        operation*=-1
    return sum    
y=sumOfSeries(n,x)
print("Sum of the series is:",y)
