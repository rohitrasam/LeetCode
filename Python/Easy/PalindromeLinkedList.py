class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
def isPalindrome(head: ListNode) -> bool:

    length = 0
    curr = head

    while curr:
        length += 1
        curr = curr.next
    

    prev, curr = None, head
    for idx in  range(length):
        if idx >= length//2:
            next = curr.next
            curr.next = prev
            prev =  curr
            curr = next
        else:
            curr = curr.next

    
    for _ in range(length//2+length%2):
        if prev.val != head.val:
            return False
        else:
            prev = prev.next
            head = head.next
    
    return True
    

h = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
ans = isPalindrome(h)
print(ans)