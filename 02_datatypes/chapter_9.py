# Set
essensial_spices = {"cardamom", "ginger", "cinnnamon"}
optional_spices = {"cloves", "ginger", "black peper"}

all_spices = essensial_spices | optional_spices # Union using (|) symbol
print(f"All spices: {all_spices}")

common_spices = essensial_spices & optional_spices # Intersection using (&) symbol
print(f"Common spices: {common_spices}")

only_in_essential = essensial_spices - optional_spices # Only in essential using (-) symbol
print(f"Only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in optional spices : {'cloves' in optional_spices}") # Find specific value