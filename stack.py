# stack implementation in Python
# stack = [1, 2, 3, 4, 5]
# stack.append(6)
#
# print(stack)
#
# # popping elements
# stack.pop()
# stack.pop(-2)
#
# print(stack)
#
# # check if stack is empty or not
# print(not stack)  # False
#
# # check the element at top
# print(stack[-1])
#
# # Get size
# print(len(stack))

def isValid(s:str):
    stack = []
    mapper = {'(': ')', '[': ']', '{': '}'}

    for c in s:
        if c in mapper:
            stack.append(c)

        else:
            if not stack:
                return False

            top = stack.pop()
            if mapper[top] !=c:
                return False

    return not stack


result = isValid("({}")
print(result)


print()
