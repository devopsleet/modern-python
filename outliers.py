data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200
print(data)
# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop) # for debugging
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) -1, -1, -1):
    if data[index] <= max_valid:
        start = index
        break


print(start)
del data[start+1:]
print(data)
