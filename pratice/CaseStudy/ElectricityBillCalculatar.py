# Case Study 1: Electricity Bill Calculator
# 1. Take input: Customer Name, Consumer Number, Units Consumed.
# 2. Calculate bill as per slab:
#    - First 100 units: Rs.5 per unit
#    - Next 100 units: Rs.7 per unit
#    - Above 200 units: Rs.10 per unit
# 3. If bill > 5000, add 5% surcharge.
# 4. Display formatted bill.
# 5. Create function: def calculate_bill(units)


name = input("Enter customer Name: ")
number = int(input("Enter Consumer Number: "))
unit_Consumed = float(input("Enter Total unit consumed: "))
def bill_calculated(unit):
    sum = 0
    if unit<=100:
        sum+=unit * 5
    elif unit<=200:
        sum = 500
        sum+=(unit-100)*7
    else:
        sum=1200
        sum+=(unit-200)*10
    return sum    
def Total_bill(x):
    if x>5000:
        x += x*0.05   
    return x 
x = bill_calculated(unit_Consumed)
y = Total_bill(x)               
print(f"Customer name:{name}\nConsumer number:{number}\nTotal Elecric bill:{y}")