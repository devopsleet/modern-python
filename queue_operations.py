import collections
queue = collections.deque()


# If you want to initialize it with some initial value
queue = collections.deque([1,2,3])

# Enqueue operations
queue.append(4)
queue.append(5)

# Dequeuing/removing elements
queue.popleft()
print(queue)

peek = queue[0]
print(peek)

print(len(queue))
