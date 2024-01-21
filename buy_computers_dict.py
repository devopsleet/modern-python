available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive"
                   }


current_choice = None
computer_parts = {} #create an empty dictionary


while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f"Removing {chosen_part}")
        print(f"Adding {chosen_part}")
        computer_parts[current_choice] = chosen_part
    else:
        print("Here is the menu")
        for key, value in available_parts.items():
            print(f"{key}: {value}")

    current_choice = input("> ")
