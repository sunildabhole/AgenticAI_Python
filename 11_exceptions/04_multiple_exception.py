def process_order(self,item, quantity):
    try:
        price = {"Masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be number")

process_order("ginger", 2)
process_order("Masala","two")
process_order("Masala",4)