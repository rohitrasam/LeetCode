from random import randint

def isBadVersion(ver):
    return bad <= ver


def firstBadVersion(n: int) -> int:
    lo =1
    hi = n

    while lo <= hi:
        mid = (hi+lo) // 2
        if isBadVersion(mid):
            hi = mid-1
        else:
            lo = mid+1
        
    return lo
    

if __name__ == '__main__':
    num = int(input())
    bad = randint(1, num)
    print(bad)
    print(firstBadVersion(num))

