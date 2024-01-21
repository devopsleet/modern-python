def sum_numbers(*args: float) ->float:
    """
    This function returns the sum of all the numerical arguments

    :*args: arguments
    """
    sum = 0
    for x in args:
        sum += x

    print(sum)

sum_numbers(12.5,3.147,98.1)
