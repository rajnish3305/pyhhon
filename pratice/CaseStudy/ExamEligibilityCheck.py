# Case Study 3: Exam Eligibility Checker
# 1. Take input: Student Name, Roll Number, Total Classes, Attended Classes.
# 2. Calculate attendance percentage.
# 3. If percentage >= 75 → Eligible, otherwise Not Eligible.
# 4. If medical certificate (Y/N), allow eligibility.
# 5. Display final result.

name = input("Enter your name: ")
Roll = int(input("Enter your roll number: "))
Total_Class = int(input("Total class taken by teacher: "))
Attended_calss = int(input("Total class attended by student: "))
medical_certificate = input("Have medical certificate (Y/N): ")
percentage = (Attended_calss/Total_Class)*100
if(medical_certificate=="Y"):
   print(f"Student name: {name}\nRoll number: {Roll}\nFor Examination: Eligible") 
elif(percentage>=75):
    print(f"Student name: {name}\nRoll number: {Roll}\nAttendace Percentage:{percentage}\nFor Examination: Eligible") 
else:
    print(f"Student name: {name}\nRoll number: {Roll}\nAttendane Percentage:{percentage}\nFor Examination: Not Eligible")     
    