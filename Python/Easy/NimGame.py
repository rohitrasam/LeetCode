def canWinNim(n: int) -> bool:
    return n % 4


if __name__ == '__main__':
    num = int(input())

    print(canWinNim(num))