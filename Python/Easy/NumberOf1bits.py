def hammingWeight(n: int) -> int:

    """Solution 1"""
    # count = 0

    # while n != 0:
    #     count = count + n % 2
    #     n >>= 1
    
    # return count

    """Solution 2"""
    #  # Initialize a counter variable to 0
    #     count = 0
    #     # Loop until n is 0
    #     while n != 0:
    #         # If the last bit of n is 1, increment the counter
    #         if n & 1 == 1:
    #             count += 1
    #         # Shift n to the right by 1 bit
    #         n = n >> 1
    #     # Return the counter
    #     return count


if __name__ == '__main__':
    num = int(input())

    print(hammingWeight(num))