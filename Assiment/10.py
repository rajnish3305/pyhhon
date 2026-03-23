n=int(input("Enter number to check Armstrong number:"))
count=0
b=a=n
while(n>0):
    count+=1
    n=n//10
sum=0    
while(a>0):
    lastdigit=a%10
    product=1
    for i in range(1,count+1):
        product*=lastdigit
    sum+=product    
    a=a//10
if(b==sum):
    print(b,"is a Armstrong number")        
else:
     print(b,"is not a Armstrong number")    