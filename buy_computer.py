available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi",
                   "dvd drive"
                   ]
#valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]

valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

print(valid_choices)
current_choice = "-"
computer_parts = []  # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        # print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains {}".format(computer_parts))
        # if current_choice == '1':
        #     computer_parts.append("computer")
        # elif current_choice == '2':
        #     computer_parts.append("monitor")
        # elif current_choice == '3':
        #     computer_parts.append("keyboard")
        # elif current_choice == '4':
        #     computer_parts.append("mouse")
        # elif current_choice == '5':
        #     computer_parts.append("mouse mat")
        # elif current_choice == '6':
        #     computer_parts.append("hdmi")
    else:
        print("Please add options from the list below:")
        # for part in available_parts:
        #     print("{0}: {1}".format(available_parts.index(part) + 1, part))
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)
