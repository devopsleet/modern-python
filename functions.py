def python_function():    print("Welcome to functions class")

python_function()


def f_name(name):
    print("Entered name : {}".format(name))
    return name * 2


f_name("gagan")


list_1 = [1,2]
new = list_1 * 2
new[1] = 3
print(new)
