# Case Study 2: Bank Simple Interest System
# 1. Take input: Customer Name, Account Number, Principal, Time.
# 2. Rate of interest:
#    - Principal < 50000 → 5%
#    - Otherwise → 7%
# 3. Calculate Simple Interest and Total Amount.
# 4. Display formatted receipt.
# 5. Create function: def calculate_interest(p, t)

name = input("Enter name: ")
number = int(input("Enter Account Number: "))
principal = int(input("Enter Principal amount: "))
time  = int(input("Time Required In Year: "))
def Simple_Intrest(principal):
    simpleIntrest = 0
    if principal<50000:
        simpleIntrest+=(principal*time*5)/100
    else:
        simpleIntrest+=(principal*time*7)/100
    return simpleIntrest
x = Simple_Intrest(principal)
Total_amount = x + principal
print(f"Customer name: {name}\nCustomer Account Number: {number}\nTotal SimpleIntrest is: {x}\nTotal Amount : {Total_amount} ")    
            