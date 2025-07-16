class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
one.next = two
two.next = three
head = one

print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next)

ptr = head
print(ptr)


# def get_sum(head):
#     ans = 0
#     while head:
#         ans = ans + head.val
#         head = head.next
#
#     return ans
#
#
# print(get_sum(head))
# def get_sum(head):
#     if not head:
#         return 0
#
#     return head.val + get_sum(head.next)

#
# print(get_sum(head))

prev_node = head.next
print(f"prev_node.val = {prev_node.val}")
add_new_node = ListNode(2.5)

print(add_new_node.val)
print(prev_node.next.val)
def add_node(prev_node, add_new_node):
    add_new_node.next = prev_node.next
    prev_node.next = add_new_node


add_node(prev_node, add_new_node)

def print_the_node_values(head):
    while head:
        print(head.val,end='')
        if head.next != None:
            print("->", end='')
        head = head.next

print_the_node_values(head)
