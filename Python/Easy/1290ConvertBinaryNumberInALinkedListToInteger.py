# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/?envType=problem-list-v2&envId=linked-list


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head: Optional[ListNode]) -> int:

    power = 0
    curr = head
    
    while curr.next:
        curr = curr.next
        power += 1
    
    res = 0

    curr = head
    while curr:
        res += 2**(power) * curr.val
        curr = curr.next
        power -= 1
    
    return res

ll = ListNode(1)
ll.next = ListNode(0)
ll.next.next = ListNode(1)
print(getDecimalValue(ll))