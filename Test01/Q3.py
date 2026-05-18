term = int(input("Enter number of terms: "))
a = 0
b = 1
while(term>0):
    print(b,end=" ")
    sum = a+b
    a = b
    b = sum
    term = term-1
    
    