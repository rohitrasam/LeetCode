# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = None
        fast = head

        while fast and fast.next:
            if slow == fast and slow:
                return True

            slow = slow.next if slow else fast.next
            fast = fast.next.next
        
        return False