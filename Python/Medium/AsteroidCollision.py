from typing import List
# Question: https://leetcode.com/problems/asteroid-collision/


def asteroidCollision(asteroids: List[int]) -> List[int]:

    rem = []

    for asteroid in asteroids:
        while rem and (asteroid < 0 and rem[-1] > 0):
            winner = asteroid + rem[-1]
            if winner < 0:
                rem.pop()
            elif winner > 0:
                asteroid = 0
            else:
                rem.pop()
                asteroid = 0
        if asteroid:
            rem.append(asteroid)
    return rem


if __name__ == '__main__':
    
    case1 = [5, 10, -5]
    case2 = [8, -8]
    case3 = [10, 2, -5]
    case4 = [-1, 3, 2, -3]
    case5 = [5, 10, -5, 8, -8, 2, -5]

    print(asteroidCollision(case1))
    print(asteroidCollision(case2))
    print(asteroidCollision(case3))
    print(asteroidCollision(case4))
    print(asteroidCollision(case5))