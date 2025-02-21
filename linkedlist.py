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
    def display():
        ptr = head
        print("*************DLL Forward direction *************")
        while ptr:
            if ptr.next:
                print(ptr.val, end="->")
            else:
                print(ptr.val)
            ptr = ptr.next
            # print(ptr.val, end="->")
            # ptr = ptr.next
            # if ptr == tail:
            #     print(ptr.val)
            #     ptr = ptr.next`

    @staticmethod
    def display_backwards():
        ptr = tail
        print("*************DLL Backward direction *************")
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

one = ListNode(20)
two = ListNode(30)
three = ListNode(40)

ListNode.add_to_start(three)
ListNode.add_to_start(two)
ListNode.add_to_start(one)
ListNode.display()
ListNode.display_backwards()
