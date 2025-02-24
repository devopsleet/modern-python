class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    @staticmethod
    def add_to_start(node_to_add):
        node_to_add.prev = head
        node_to_add.next = head.next
        head.next.prev = node_to_add
        head.next = node_to_add

    @staticmethod
    def add_to_end(node_to_add):
        node_to_add.next = tail
        node_to_add.prev = tail.prev
        tail.prev.next = node_to_add
        tail.prev = node_to_add

    @staticmethod
    def display():
        ptr = head
        print("************* Displaying DLL in Forward direction **************")
        while ptr:
            if ptr.next:
                print(ptr.val, end="->")
            else:
                print(ptr.val)
            ptr = ptr.next

    @staticmethod
    def display_backwards():
        ptr = tail
        print("************* Displaying DLL in Backward direction *************")
        while ptr:
            if ptr.prev:
                print(ptr.val, end="<-")
            else:
                print(ptr.val)
            ptr = ptr.prev


head = ListNode('head')
tail = ListNode('tail')
head.next = tail
tail.prev = head

first = ListNode(10)
second = ListNode(20)
third = ListNode(30)
fourth = ListNode(40)
fifth = ListNode(50)
sixth = ListNode(60)

ListNode.add_to_start(fifth)
ListNode.add_to_start(fourth)
ListNode.add_to_start(third)
ListNode.add_to_start(second)
ListNode.add_to_start(first)
ListNode.add_to_end(sixth)

ListNode.display()
ListNode.display_backwards()
