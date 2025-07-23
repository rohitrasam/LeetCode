# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2
    if len(A) > len(B):
        A, B = B, A
    
    l, r = 0, len(A) - 1
    
    while True:
        m_A = (l + r) // 2
        m_B = half - m_A - 2

        Aleft = A[m_A] if m_A >=0 else float("-inf")
        Aright = A[m_A+1] if m_A + 1 < len(A) else float("inf")
        Bleft = B[m_B] if m_B >=0 else float("-inf")
        Bright = B[m_B+1] if m_B+1 < len(B) else float("inf")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
               return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = m_A - 1
        else:
            l = m_A + 1
    

if __name__ == '__main__':

    case1 = [1,3], [2]
    case2 = [1,2], [3,4]

    print(findMedianSortedArrays(*case1))
    print(findMedianSortedArrays(*case2))