class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def calc_sum(self, head):

        sum = 0
        while head:
            sum = sum + head.val
            head = head.next
        print(sum)

    def recursive_calc_sum(self, head):

        if not head:
            return 0

        return head.val + self.recursive_calc_sum(head.next)

    def get_middle_node(self, head):
        length = 0
        dummy = head

        while dummy:
            length += 1
            dummy = dummy.next

        for _ in range(length // 2):
            head = head.next

        return head.val

    def get_middle_node_method2(self,head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.val


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
head = one

head.calc_sum(head)

print("""The sum of all  the linkedlist nodes
 calculated through recursive methid is {0}"""
      .format(head.recursive_calc_sum(head)))

print(head.get_middle_node(head))

print(head.get_middle_node_method2(head))
