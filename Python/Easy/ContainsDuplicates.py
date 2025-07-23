def containsDuplicates(arr: list[int]) -> bool:
    counter = []
    arr.sort()
    for item in arr:
        if item in counter:
            return False
        counter.append(item)
    return True


if __name__ == '__main__':
    a = list(int, input().split())

    print(containsDuplicates(a))