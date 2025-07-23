class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode):

    curr = head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
re = reverseList(h)
while re:
    print(re.val)
    re = re.next