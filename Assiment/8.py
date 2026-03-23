n=int(input("Enter number:"))
def palimdrom(n):
    a=n
    lastdigit=0
    while(n>0):
        lastdigit*=10
        lastdigit+=n%10
        n=n//10
    if lastdigit==a:
        return True
    else:
        return False   
x=palimdrom(n) 
print(x)    