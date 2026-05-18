# n = int(input("Enter number: "))
# 100 to 1
# while n>0 :
#     print(n)
#     n-=1

# 1 to 100
# i=1
# while i<=n:
#     print(i)
#     i+=1

# Table of any number
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1

# suare number 1 to 100
# i=1
# while i<=10:
#     print(i**2)
#     i+=1

# search any number x in tupple
tupple = (1,4,9,16,81,36,49,64,81,100)
x = int(input("Enter number to search: "))
i=0
while i<len(tupple):
    if x!=tupple[i]:
        i+=1
        continue
    print(x,"is at",i,"index") 
    i+=1    
    
    

    