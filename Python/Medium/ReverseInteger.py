def reverse(x: int):
    temp = x if x > 0 else abs(x)
    rev_num = 0
    while temp != 0:
        rem = temp % 10
        rev_num = rem + rev_num * 10
        temp //= 10
    
    rev_num = -rev_num if x < 0 else rev_num

    return rev_num if rev_num.bit_length()<=31 else 0


if __name__ == '__main__':
    num = int(input())

    print(reverse(num))