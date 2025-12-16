order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 300 else 30 # ternary operator
print(f"Your delivery fees: {delivery_fees}")