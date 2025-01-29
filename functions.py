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

# lambda functions can take any number of arguments

lambda a,b: a + b

sub = lambda *a: sum(a)
print(sub(12,3))


def f1():
    return 10

print(f1)
print(type(f1))
print(f1())


f2 = lambda : 10

print(f2)
print(f2())


# filter(function, iterable)

scores = [12,34,56,67,89,100]
def f3(x):
    if x > 40:
        return True
    else:
        return False


filtered_list = filter(f3, scores)
for val in filtered_list:
    print(val)


print(bool(0))
