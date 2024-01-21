shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))


a = b = c = another_list

print(a)
print(b)
print(c)

b.append("cream")
print(c)
