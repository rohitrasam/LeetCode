def isHappy(n: int) -> bool:
    memo = set()

    while n != 1:
        n = sum(list(map(lambda x: int(x)**2, str(n))))
        if n in memo:
            return False
        memo.add(n)
        
    return True

    




if __name__ == '__main__':
    num = int(input())

    print(isHappy(num))

