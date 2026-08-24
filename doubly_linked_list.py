class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.Next = None

    def add_to_start(self, node_to_add):
        nextNode = head.next
        node_to_add.next = nextNode
        node_to_add.prev = head
        head.next = node_to_add
        nextNode.prev = node_to_add

    def add_to_end(self, node_to_add):
        prevNode = tail.prev
        node_to_add.next = tail
        node_to_add.prev = prevNode
        tail.prev = node_to_add
        prevNode.next = node_to_add


head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head
