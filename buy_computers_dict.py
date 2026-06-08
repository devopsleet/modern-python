available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive"
                   }

current_choice = None
compuetr_parts =  {}


while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in compuetr_parts:
            compuetr_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            compuetr_parts[current_choice] = chosen_part
    else:
        print("Please add options from the list")
        for key,value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")
