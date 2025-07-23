from typing import List

def longetWPI(hours: list[int]) -> int:
    res = score = 0
    seen = {}

    for i, h in enumerate(hours):
        score = score + 1 if h > 8 else score - 1
        if score > 0:
            res = i + 1
        seen.setdefault(score, i)
        if score - 1 in seen:
            res = max(res, i - seen[score-1])
    return res

if __name__ == '__main__':
    
    case1 = [6, 10, 11, 9, 8, 8, 6, 11, 11]
    print(longetWPI(case1))