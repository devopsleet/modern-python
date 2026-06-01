numbers = (0,1,2,3,4,5)


print(*numbers)


def test_star(*args):
    print(args)
    for x in args:
        print(x)

test_star(0,1,2,3,34,5)


test_star()
