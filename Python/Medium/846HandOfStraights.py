# https://leetcode.com/problems/hand-of-straights/description/


from typing import List
from collections import Counter

def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    
    counter: Counter = Counter(hand)
    hand.sort()

    for i in hand:
        if counter[i] == 0:
            continue
        counter[i] -= 1
        for j in range(1, groupSize):
            if i + j in counter and counter[i+j] != 0:
                counter[i+j] -= 1
            else: 
                return False

    return True




if __name__ == '__main__':

    case = [3,4,7,4,6,3,6,5,2,8], 2
    print(isNStraightHand(*case))
    case = [2,3,1], 3
    print(isNStraightHand(*case))

    case = [1,2,3,6,2,3,4,7,8], 3
    print(isNStraightHand(*case))
    case = [1,2,3,4,5], 4
    print(isNStraightHand(*case))
