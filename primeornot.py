def prime(num):
    if num == 1:
        print("no")
        return
    if num == 2:
        print("Yes")
        return
    i = 2
    while i * i <= num:
        if num % i == 0:
            print('no')
            return
        i += 1
    print("yes")


prime(73)
