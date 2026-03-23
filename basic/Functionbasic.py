# n=10
# for i in range(n):
#     if i==7 :
#         pass # if we commentout pass then give error b/c if we introduce if then must initialise some value
#     print(i)



import random
value = random.randint(1,10) # value take int 1 to 10 include 1 and 10 both
# value=random.random() # give random value b/w 0 and 1 excluding 0 and 1 give float value
print(value)
count=0
while True:
    n=float(input("n: "))
    count+=1
    if n==value:
        print(count)
        break
   

    