# List

ingradients = ["water", "milk", "black tea"]
ingradients.append("sugar") # Add new element in list in the last
print(f"Ingradients are: {ingradients}")
ingradients.remove("water") # Remove any specific element in list
print(f"Ingradients are: {ingradients}")

spice_options = ["ginger", "cardamom"]
chai_igradients = ["water", "milk"]

chai_igradients.extend(spice_options) # Combine two or more lists
print(f"chai: {chai_igradients}")
chai_igradients.insert(2, "black tea") # Add new element in the specific index
print(f"chai: {chai_igradients}")

last_added = chai_igradients.pop() # Remove last element
print(f"{last_added}")
print(f"chai: {chai_igradients}")
chai_igradients.reverse() # Reverse alllist
print(f"chai: {chai_igradients}")
chai_igradients.sort() # Sorting list
print(f"chai: {chai_igradients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level is: {max(sugar_levels)}") # Find Maximum in list
print(f"Minimum sugar level is: {min(sugar_levels)}") # Find Minimum in list

base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")