available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive"
                   }




current_choice = None
while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
    else:
        print("Your choice s not in the dictionary")
        for keys, values in available_parts.items():
            print(keys, values)
        print("0: to finish")

    current_choice = input("> ")
