# https://leetcode.com/problems/plates-between-candles/description/


from typing import List


def platesBetweenCandles(s: str, queries: List[List[int]]) -> List[int]:

    res = []
    # figure out left and right most candles
    candles = []
    candlesMap = {}
    counter = 0
    closestR = [len(s)] * len(s)
    closestL = [-1] * len(s)

    lastCandle = -1

    for idx, char in enumerate(s):
        if char == "|":
            candles.append(idx)
            candlesMap[idx] = counter
            counter += 1
            lastCandle = idx
        closestL[idx] = lastCandle
    lastCandle =  len(s)

    for idx in range(len(s)-1, -1, -1):
        if s[idx] == "|":
            lastCandle = idx
        closestR[idx] = lastCandle

    # figure out # of plates in between left and right most candles
    # right modst - left most candle -1 - # of candles in between candles

    for l, r in queries:
        l_candle, r_candle = closestR[l], closestL[r]
        plates = r_candle - l_candle - 1
        plates -= candlesMap.get(r_candle, 0) - candlesMap.get(l_candle, 0) - 1
        res.append(max(plates, 0))
    
    return res
     


if __name__ == '__main__':
    case = "**|**|***|", [[2,5],[5,9]]
    print(platesBetweenCandles(*case))
    case = "***|**|*****|**||**|*", [[1,17],[4,5],[14,17],[5,11],[15,16]]
    print(platesBetweenCandles(*case))
