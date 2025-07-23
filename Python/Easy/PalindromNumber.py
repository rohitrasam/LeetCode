def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    num = x
    rem = 0

    while x != 0:
        rem += x % 10
        x //= 10
        if num == rem:
            return True
        rem *= 10
    
    return False
    



if __name__ == '__main__':
    num = int(input())
    print(isPalindrome(num))