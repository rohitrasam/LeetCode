# https://leetcode.com/problems/repeated-dna-sequences/description/?envType=problem-list-v2&envId=sliding-window


from typing import Dict, List, Set


def findRepeatedDnaSequences(s: str) -> List[str]:
    # seq_count: Dict[str, int] = {}
    # res: Set = set()
    # l = 0
    # for r in range(9, len(s)):
    #     seq = s[l:r+1]
    #     seq_count[seq] = seq_count.get(seq, 0) + 1
    #     if seq not in res and seq_count[seq] >= 2:
    #         res.add(seq)
            
    #     l += 1
    # return list(res)

    seq_count: Dict[str, int] = {}
    res: List = []
    l = 0
    for r in range(9, len(s)):
        seq = s[l:r+1]
        seq_count[seq] = seq_count.get(seq, 0) + 1        
        l += 1
    
    for seq in seq_count:
        if seq_count[seq] > 1:
            res.append(seq)
    return res


if __name__ == '__main__':

    case = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(findRepeatedDnaSequences(case))
    case = "AAAAAAAAAAAAA"
    print(findRepeatedDnaSequences(case))