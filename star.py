numbers = (0,1,2,3,4,5)

# print(numbers, sep=";")
#
# print(*numbers, sep=";")
# print(0,1,2,3,4,5, sep="-")


def test_scores(*args):
    print(args)
    print(*args)


test_scores(0,1,2)
test_scores()
