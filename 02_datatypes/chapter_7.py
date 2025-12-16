# Tuples
masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2,spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")


ginger_ratio, cardamon_ratio = 2, 1
print(f"Ratio is Ginger: {ginger_ratio} and Cardamom: {cardamon_ratio}")
ginger_ratio, cardamon_ratio = cardamon_ratio, ginger_ratio
print(f"Ratio is Ginger: {ginger_ratio} and Cardamom: {cardamon_ratio}")

# Membership

print(f"Is ginger in masala spices ? {'cinnamon' in masala_spices}")