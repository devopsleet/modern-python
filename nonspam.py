menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for item_list in menu:
    if "spam" not in item_list:
        print(item_list)
    else:
        for idx in range(len(item_list)-1, -1,-1):
            if item_list[idx] == "spam":
                del item_list[idx]
        print(item_list)


# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end = " ")
#     print()
