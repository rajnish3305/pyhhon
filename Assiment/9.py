n=int(input("Enter number:"))
def sumOfDigit(n):
    lastdigit=0
    sum=0
    while(n>0):
        lastdigit=n%10
        sum+=lastdigit
        n=n//10
    return sum   
x=sumOfDigit(n) 
print("Sum of digits are:",x)  