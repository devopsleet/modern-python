import hashlib

# print(sorted(hashlib.algorithms_guaranteed))
# print(sorted(hashlib.algorithms_available))

python_program = """for i in integer(10):
"""

print(python_program)

original = hashlib.sha256(python_program.encode('utf8'))
print(original)
