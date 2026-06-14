import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}

# Perform a shallow copy
things = copy.deepcopy(animals)

# Perform a deep copy

#things = animals.copy()
# things["teddy"] = ["toy"]

print(animals["teddy"])
print(things["teddy"])

print()

things["teddy"].append("toy")

print(animals["teddy"])
print(things["teddy"])
