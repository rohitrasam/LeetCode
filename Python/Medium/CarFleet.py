from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    pos_speed = [(pos, vel) for pos, vel in zip(position, speed)]
    pos_speed.sort(reverse=True)
    stack = [pos_speed[0]]
    for car in pos_speed[1:]:
        if stack and (target - car[0]) / car[1] > (target - stack[-1][0]) / stack[-1][1]:
            stack.append(car)

    
    return len(stack)
    


if __name__ == '__main__':

    case1 = 12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]
    case2 = 10, [3], [3]
    case3 = 100, [0, 2, 4], [4, 2, 1]
    case4 = 10, [8, 3, 7, 4, 6, 5], [4, 4, 4, 4, 4, 4]
    case5 = 20, [6, 2, 17], [3, 9, 2]
    case6 = 31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,4,9,7,6,4]
    case7 = 10, [4, 6], [3, 2]
    print(carFleet(*case1))
    print(carFleet(*case2))
    print(carFleet(*case3))
    print(carFleet(*case4))
    print(carFleet(*case5))
    print(carFleet(*case6))
    print(carFleet(*case7))