# String, Indexing, Slicing
chai_type = "Ginger chai"
customer_name = "priya"

print(f"Order for {customer_name} : {chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"First Word : {chai_description[0:8]}")
print(f"First Word : {chai_description[12:]}")
print(f"First Word : {chai_description[::-1]}") # Reversing the hole string

label_text = "Chai $pecial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Ecoded label: {ecoded_label}")
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label : {decoded_label}")
