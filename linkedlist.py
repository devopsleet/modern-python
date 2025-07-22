class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self. prev = None


head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head

One = ListNode(10)
two = ListNode(20)
three = ListNode(30)
four = ListNode(40)
five = ListNode(50)
def add_to_start(node_to_add):
    node_to_add.next = tail
    node_to_add.prev = head
    head.next = node_to_add
    tail.prev = node_to_add


add_to_start(One)


def add_to_end(node):
    node.next = tail
    node.prev = tail.prev
    tail.prev.next = node
    tail.prev = node


add_to_end(two)
add_to_end(three)
add_to_end(four)
add_to_end(five)
def remove_from_start():
    if head.next == tail:
        return
    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next


#remove_from_start()

def get_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val
def printLinkedList(head):
    while head:
        print(head.val, end="")
        if head.next:
            print("->",end="")

        head = head.next

if __name__ == "__main__":
    printLinkedList(head)
    print()
    #remove_from_start()
    #print()
    printLinkedList(head)
    print()
    ans = get_middle(head)
    print(ans)
