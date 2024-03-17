available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive"
                   }

choice = None
computer_parts = []

while choice != '0':
    if choice in available_parts:
        chosen_part = available_parts[choice]
        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)
        else:
            computer_parts.append(chosen_part)
            print(f"Your list now contains: {computer_parts}")
    else:
        print("Printing the original dictionary")
        for key, values in available_parts.items():
            print(f"{key} : {values}")
        print("0: to finish")

    choice = input("> ")
