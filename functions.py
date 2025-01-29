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


def f_name(name):
    print("Enter name = {}".format(name))
    return name * 10


return_val = f_name("Gagan")
print(return_val)
print(type(return_val))


def f_name(name):
    print("Enter name = {}".format(name))
    return name * 10


return_val = f_name([1,2,3])
print(return_val)
print(type(return_val))


def string_concat(*args):
    print(args)
    print(type(args))


string_concat("")


# keyword arguments

# lambda functions

def normalFunc(x):
    return x * x


result = normalFunc(2)
print(result)

print(type(normalFunc))

lambda x: x ** 2

a = lambda x: x **2
print(type(a))
print(a(12))
