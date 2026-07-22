class ListNode:
    def __init__(self, val):
        self. val = val
        self. link = None

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two
two.next = three

head = one

print(head.val)
