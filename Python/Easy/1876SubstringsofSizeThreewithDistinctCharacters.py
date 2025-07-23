# https://leetcode.com/classic/problems/substrings-of-size-three-with-distinct-characters/description/


def countGoodSubstrings(s: str) -> int:

    good = 0
    for i in range(len(s)-2):
        if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
            good += 1

    return good

if __name__ == '__main__':

    case = "xyzzaz"
    print(countGoodSubstrings(case))

    case = "aababcabc"
    print(countGoodSubstrings(case))