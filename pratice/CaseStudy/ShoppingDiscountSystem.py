# Case Study 4: Shopping Discount System
# 1. Take input: Customer Name, Product Price, Quantity.
# 2. Calculate Total Amount.
# 3. Apply discount:
#    - Above 5000 → 10%
#    - 2000–5000 → 5%
#    - Below 2000 → No discount
# 4. Display final bill.
# 5. Create function: def calculate_discount(total)

name = input("Enter customer name: ")
product_price = float(input("Enter price of product: "))
Quantity = int(input("total Quantity: "))
Total_amount = Quantity * product_price
Total_MRP_Amount = Total_amount
if(Total_amount>5000):
    Total_amount -=Total_amount*0.1
elif(Total_amount>=2000):
    Total_amount -=Total_amount*0.05
else:
    Total_amount-=0
Discount = Total_MRP_Amount - Total_amount
print(f"Customer Name:{name}\nPrice per Product:{product_price}\nTotal Quantity:{Quantity}\nTotal MRP Amount:{Total_MRP_Amount}\nTotal Discount:{Discount}\nTotal Bill:{Total_amount}")    
        
        