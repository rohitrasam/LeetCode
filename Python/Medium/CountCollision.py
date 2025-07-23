# Question: https://leetcode.com/problems/count-collisions-on-a-road/


def countCollisions(directions: str) -> int:

    # collision: R -><- L, R -> S, S <- L,
    # no collision: L <--> R, S -> R, L <- S 

        left_c = right_c = 0
        ans = 0
        for car in directions:
            if car == 'L':
                ans += left_c
            else:
                left_c = 1
        
        for car in directions[::-1]:
            if car == 'R':
                ans += right_c
            else:
                right_c = 1
        
        return ans

if __name__ == '__main__':
    
    case1 = "RLRSLL"
    case2 = "LLRR"
    case3 = "LRRSLL"
    case4 = "SLRSLL"
    case5 = "LLRSLL"
    case6 = "LLLLLLRSRSLLLRSRSSRRLRRRRRRRRRR"

    print(countCollisions(case1))
    print(countCollisions(case2))
    print(countCollisions(case3))
    print(countCollisions(case4))
    print(countCollisions(case5))
    print(countCollisions(case6))