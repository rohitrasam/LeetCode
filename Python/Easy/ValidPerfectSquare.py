def isPerfectSquare(num: int):

    return (num ** 0.5) % 1 == 0


if __name__ == '__main__':
    n = int(input())

    print(isPerfectSquare(n))
