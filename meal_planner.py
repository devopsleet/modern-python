from contents import pantry, recipes

# print(pantry)
# print(recipes)


display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display a menu of the recipes
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        shopping_list = {}
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\t You need to buy {quantity_to_buy} of {food_item}")
                shopping_list[food_item] = quantity_to_buy
        print(shopping_list)
