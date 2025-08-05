from collections import deque

dq = deque()
print(dq)

dq.append(1)
print(dq)

dq.append(2)
print(dq)


dq.append(3)
print(dq)


dq.appendleft(-1)
dq.appendleft(-2)

print(dq)


dq.appendleft(-3)
print(dq)


dq.popleft()
print(dq)


list = [7,8,9]
dq.extend(list)
print(dq)

dq.extendleft(list)
print(dq)


dq.reverse()

print(dq)


print(dq.count(9))
dq.remove(8)
print(dq)
