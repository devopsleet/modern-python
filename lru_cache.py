class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity.head = ListNode(-1, -1)
        self.capacity.tail = ListNode(-2, -3)
        self.capacity.




    def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:
