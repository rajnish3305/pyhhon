phy = int(input("Enter physics marks: "))
chem = int(input("Enter chemistry marks: "))
math = int(input("Enter maths marks: "))
marks ={}
marks.update({"physics" : phy})
marks.update({"chemistry" : chem})
marks.update({"maths" : math})

print(marks)
