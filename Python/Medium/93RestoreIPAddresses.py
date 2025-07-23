# https://leetcode.com/problems/restore-ip-addresses/description/?envType=problem-list-v2&envId=backtracking

from typing import List


def restoreIpAddresses(s: str) -> List[str]:
    res: List[str] = []
    if len(s) > 12:
        return res

    def bt(idx: int, dots: int, cur_ip: str) -> None:
        if dots == 4 and idx == len(s):
            res.append(cur_ip[:-1])
            return

        if dots > 4:
            return

        for j in range(idx, min(idx + 3, len(s))):
            if int(s[idx : j + 1]) <= 255 and (idx == j or s[idx] != "0"):
                bt(j + 1, dots + 1, cur_ip + s[idx:j + 1] + ".")

    bt(0, 0, "")
    return res


if __name__ == "__main__":
    case = "25525511135"
    print(restoreIpAddresses(case))
    case = "0000"
    print(restoreIpAddresses(case))
    case = "101023"
    print(restoreIpAddresses(case))
