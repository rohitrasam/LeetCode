def singleNumber(nums: list[int]) -> int:

    count ={}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    return sorted(count.items(), key=lambda x: x[1])[0][0]  # list(filter(lambda x: x[1] == 1, count.items()))[0][0]
    




if __name__ == '__main__':

    n = list(map(int, input().split()))


    print(singleNumber(n))