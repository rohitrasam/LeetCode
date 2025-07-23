def plusOne(digits: list[int]) -> list[int]:
    """
    digits = ''.join(map(str, (digits)))
    digits = int(digits) + 1
    digits = list(str(digits))
    return list(map(str, digits))
    """

    return list(map(int, list(str(int("".join(map(str, digits))) + 1))))


if __name__ == '__main__':
    nums = list(map(int, input().split()))

    print(plusOne(nums))