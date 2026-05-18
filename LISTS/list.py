
# list = [[10,20],[30,40]]
# list1 = list      
# print(id(list))
# print(id(list1)) 

list = [[10,20],[30,40]]
list1 = []
for i in list:
    for j in i:
        list1.append(j)
print()       
print(list)
print(list1) 


list = []
for i in range(0,2):
    list1=[]
    for j in range(0,2):
        list1.append(int(input("Enter number")))
    list.append(list1)
print(list)        
