def banner_text(text: str = "", screen_width: int = 80) -> None:
    """
    Get a text as input from user and print it on the screen with the screen width param

    :param text: Text string provided by the user
    :param screen_width: width of the screen
    :return: Does not return anything
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified width".format(text, screen_width))
        # print("EEK!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*", 6)
banner_text("Always look on the bright side of life...", 50)
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")

# result = banner_text("Nothing is returned")
# print(result)
#
# numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
# print(numbers.sort())
