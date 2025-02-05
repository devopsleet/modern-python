class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


one = ListNode(1)
print(one)

two = ListNode(2)

three = ListNode(3)

one.next = two
two.next = three
head = one.next

print(head.val)
print(head.next.val)
