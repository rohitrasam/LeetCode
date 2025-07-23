from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:

    stack = []
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        curr = temperatures[i]
        while stack and curr > stack[-1][0]:
            temp, idx = stack.pop()
            res[idx] = i - idx
        stack.append([temperatures[i], i])
    
    return res

if __name__ == '__main__':

    case1 = [73,74,75,71,69,72,76,73]
    case2 = [30,40,50,60]
    case3 = [30,60,90]

    print(dailyTemperatures(case1))
    print(dailyTemperatures(case2))
    print(dailyTemperatures(case3))