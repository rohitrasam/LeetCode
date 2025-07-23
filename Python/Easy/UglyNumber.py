def isUgly(n: int) -> bool:
    # while n%2 == 0 and n!= 0:
    #     n //= 2
    # while n%3 == 0 and n!= 0:
    #     n //= 3
    # while n%5 == 0 and n!= 0:
    #     n //= 5
    # return n == 1
    if n == 0:
        return False
    for x in [2, 3, 5]:
        while n%x == 0:
            n //= x
    return n == 1
if __name__ == '__main__':
    num = int(input())

    print(isUgly(num))