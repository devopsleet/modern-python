batting_order = ["Rohit", "Virat", "Sachin", "Pant", "Sky"]

batting_order.append("Jaiswal")
print(batting_order)


print(len(batting_order))
batting_order.insert(8, "Gagan")
print(batting_order)


batting_order.insert(-2, "Tejas")
print(batting_order)


input_user = input("Enter the input ")
print(type(input_user))


How to convert the user input to a list

input_user_list_format = input_user.split()
print(input_user_list_format)
print(type(input_user_list_format))


new_string = "LiveAuctioners"
new_string[5:2] = "sss"

print(new_string)


new_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(new_list[4:2])
new_list[4:2] = ['x', 'y', 'z']
print(new_list)
