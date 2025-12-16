# Dictionary
chai_order = dict(type="Masala chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea" # Add any key-value in dictionary
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe liquid: {chai_recipe['liquid']}")
print(f"Recipe: {chai_recipe}")

del(chai_recipe["liquid"]) # Delete/Remove any value from dictionary

print(f"Is sugar in the order: {'sugar' in chai_order}") # Find specific item in dict

chai_order = {"type":"Ginger chai", "size":"Medium", "sugar":1}

print(f"Order details (keys): {chai_order.keys()}") # See only keys 
print(f"Order details (values): {chai_order.values()}") # See only values 
print(f"Order details (items): {chai_order.items()}") # See only items

last_item = chai_order.popitem() # Remove last item in dictionary
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "Crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices) # Update any dictionary
print(f"Updated chai recipe: {chai_recipe}")

chai_size = chai_order["size"]
print(f"Chai size is: {chai_size}")

customer_note = chai_order.get("size", "no note")
print(f"Customer note is: {customer_note}")