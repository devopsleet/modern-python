class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

one.next = two
two.prev = one
two.next = three
three.prev = two


node =

def add_node(node, node_to_add):
    one.next = two
    two.next = three
    three.next = None
    three.prev =
