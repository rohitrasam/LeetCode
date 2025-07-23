def minCostClimbingStairs(costs: list[int]) -> int:

    p2, p1 = costs[0], costs[1]
    for idx in range(2, len(costs)):
        curr = costs[idx] + min(p2, p1)
        p2, p1 = p1, curr
    
    return min(p2, p1)






if __name__ == '__main__':
    cost = list(map(int, input().split()))

    print(minCostClimbingStairs(cost))