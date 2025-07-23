# https://leetcode.com/problems/binary-watch/?envType=problem-list-v2&envId=backtracking


from typing import List


def readBinaryWatch(turnedOn: int) -> List[str]:
    res = []

    for h in range(12):
        for m in range(60):
            if (bin(h).count("1") + bin(m).count("1")) == turnedOn:
                res.append("{}:{:02d}".format(h,m))
    return res


if __name__ == '__main__':

    case = 1
    print(readBinaryWatch(case))
    case = 2
    print(readBinaryWatch(case))
    case = 9
    print(readBinaryWatch(case))
