# https://leetcode.com/problems/letter-case-permutation/?envType=problem-list-v2&envId=backtracking


from typing import List, Set


def letterCasePermutation(s: str) -> List[str]:
    ans: Set[str] = set()

    def bt(i: int, curr: str) -> None:
        if i >= len(s):
            ans.add(curr)
            return

        while i < len(s) and s[i].isdigit():
            curr += s[i]
            i += 1

        if i < len(s):
            bt(i + 1, curr + s[i])
            bt(i + 1, curr + s[i].upper())
        else:
            ans.add(curr)

    bt(0, "")
    return list(ans)


if __name__ == "__main__":
    case = "c"
    print(letterCasePermutation(case))
    case = "a1b2"
    print(letterCasePermutation(case))
    case = "a12b2c3d"
    print(letterCasePermutation(case))
    case = "a1b2c3d"
    print(letterCasePermutation(case))
    case = "a1b2c3"
    print(letterCasePermutation(case))
    case = "3z4"
    print(letterCasePermutation(case))
