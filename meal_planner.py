from contents import pantry, recipes

# print(pantry)
# print(recipes)


display_dict = {}
buy_ingredients = {}


def new_ingredients_to_buy(food_item_new, value):
    buy_ingredients[food_item_new] = value


for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display a menu of the recipes
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected the {selected_item}")
        print("checking ingredients:")
        ingredients = recipes[selected_item]
        print(ingredients)

        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"{food_item}")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"No item {quantity_to_buy} of {food_item}")
                new_ingredients_to_buy(food_item, quantity_to_buy)

for item, value in buy_ingredients.items():
    print(item, value)
