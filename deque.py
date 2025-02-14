from collections import deque

dq = deque()

print(dq)

# append operation

dq.append(5)
dq.append(10)

print(dq)

# appendleft(x)

dq.appendleft(4)
#dq.appendleft(3)

print(dq)


# pop operation
# remove from the right end and returns the element

popped = dq.pop()
print(popped)
print(dq)

# Extend operation

dq.extend([30,40,50])
dq.extend((70, 80))
print(dq)

# extendleft(iterables) elements are added from the left in reverse order

dq.extendleft([1,2,3])

print(dq)

# rotate(n) - rotate the deque

dq.rotate(2)
print(dq)

dq.rotate(-2)
print(dq)
