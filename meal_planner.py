from contents import pantry, recipes

# print(pantry)
# print(recipes)


display_dict = {}

for index, key in enumerate(recipes):
    display_dict[str(index+1)] = key

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-----------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected  {selected_item}")
        print("checking ingredients")
        ingredients = recipes[selected_item]
        print(ingredients)
        need_to_by = {}
        for ingredient, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(ingredient, 0)
            if required_quantity < quantity_in_pantry:
                print(f"{ingredient} OK")
            else:
                quantity_delta = required_quantity - quantity_in_pantry
                need_to_by[ingredient] = need_to_by.get(ingredient,quantity_delta)
