# https://leetcode.com/problems/swap-nodes-in-pairs/description/?envType=problem-list-v2&envId=linked-list


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    p1 = head
    p2 = head.next
    ret_head = p2
    prev_n = None

    while p2:
        # 1 - 2 - 3 - 4
        # p1  p2  n 
        next_n: ListNode = p2.next
        p2.next = p1
        p1.next = next_n
        if prev_n:
            prev_n.next = p2
        prev_n = p1
        p1 = next_n
        p2 = next_n.next if next_n else None

    return ret_head


if __name__ == '__main__':

    case = ListNode(1)
    case.next = ListNode(2)
    case.next.next = ListNode(3)
    case.next.next.next = ListNode(4)
    case.next.next.next.next = ListNode(5)
    case.next.next.next.next.next = ListNode(6)
    
    ret = swapPairs(case)

    while ret:
        print(ret.val, end=(" -> " if ret.next else ""))
        ret = ret.next