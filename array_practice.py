arr = [3,5,4,1,9]


def min_max(arr):
    if len(arr) == 1:
        return arr

    minimum = maximum = arr[0]

    for i in range(2, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
        if arr[i] < minimum:
            minimum = arr[i]


    print(minimum)
    print(maximum)


min_max(arr)
