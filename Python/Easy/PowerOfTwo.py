def isPowerOfTwo(n: int) -> bool:

    if n == 0:
        return False
    if n == 1:
        return True
    if n % 2 == 1:
        return False
    return isPowerOfTwo(n/2)

if __name__ == '__main__':
    num = int(input())

    print(isPowerOfTwo(num))