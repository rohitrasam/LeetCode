import math
class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        high = -math.inf 


        # high = max(total, high)
        nums.insert(0, nums.pop())
        
        return high
    
sol = Solution()
n = [4, 3, 2, 6]
print(sol.maxRotateFunction(n))