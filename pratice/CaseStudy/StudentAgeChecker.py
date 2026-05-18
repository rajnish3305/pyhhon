# Case Study 5: Student Age Category Checker
# 1. Take input: Student Name and Age.
# 2. Categorize:
#    - Below 13 → Child
#    - 13–19 → Teen
#    - 20–59 → Adult
#    - 60+ → Senior
# 3. Display category.
# 4. Create function: def find_category(age)

name = input("Enter Student name: ")
age = int(input("Enter age of student: "))
def find_category(age):
    if age>=60:
        return "Senior"
    elif age>=20:
        return "Adult"
    elif age>=13:
        return "Teen"
    else:
        return "Child"
Category = find_category(age) 
print(f"Student Name:{name}\nStudent Age:{age}\nStudent Category:{Category}")   
