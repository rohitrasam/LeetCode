# https://leetcode.com/problems/count-numbers-with-unique-digits/description/?envType=problem-list-v2&envId=backtracking


def countNumbersWithUniqueDigits(n: int) -> int:

    """ My solution """
    if n <= 1:
        return 1 if n == 0 else 10

    res = 0
    def dfs(count: int, place: int) -> int:
        if place == 1:
            return count * 9

        count *= dfs(count - 1, place - 1)
        return count

    for i in range(n-1, 0, -1):
        res += dfs(9, i)

    return res + 10

    """ Leetcode Solution: https://leetcode.com/problems/count-numbers-with-unique-digits/solutions/4944371/math-beats-100-00-simple-code-explanation-python-c-c-java """
    if n == 0: return 1
    total = 10
    prod = 9
    for i in range(2, n + 1):
        total += prod * (11 - i)
        prod *= 11 - i
    return total

if __name__ == '__main__':

    case = 4
    print(countNumbersWithUniqueDigits(case))
    case = 2
    print(countNumbersWithUniqueDigits(case))
    case = 0
    print(countNumbersWithUniqueDigits(case))
    case = 3
    print(countNumbersWithUniqueDigits(case))
