# https://leetcode.com/problems/rings-and-rods/


from typing import Dict, List, Set


def countPoints(rings: str) -> int:
    rods: Dict[str, Set['str']] = {}
    rings: List[str] = list(rings)
    count: int = 0
    
    for pair in range(0, len(rings), 2):
        col, rod = rings[pair:pair+2]
        if rod in rods:
            rods[rod].add(col)
        else:
            rods[rod] = {col}
    
    for rod in rods:
        if len(rods[rod]) == 3:
            count += 1

    return count


if __name__ == '__main__':

    case1 = "B0B6G0R6R0R6G9"
    case2 = "B0R0G0R9R0B0G0"
    case3 = "G4"    
    print(countPoints(case1))    
    print(countPoints(case2))    
    print(countPoints(case3))