n=int(input("Enter 1st number:"))
m=int(input("Enter 2nd number:"))
def least(n,m):
    if n>m:
        return m
    else:
        return n
y=least(n,m)
print("Least number is ",y)