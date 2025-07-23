def climbStairs(num: int) -> int:

    """Dynamic Program"""
    dp = [0]*(num+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, num+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[num]

    """Recursion"""
    # memo = {}
    # memo[1] = 1
    # memo[2] = 2

    # def climb(steps: int):

    #     if steps in memo:
    #         return memo[steps]
        
    #     memo[steps] = climb(steps - 1) + climb(steps-2)

    #     return memo[steps]

    # return climb(num)


if __name__ == '__main__':

    n = int(input())

    print(climbStairs(n))