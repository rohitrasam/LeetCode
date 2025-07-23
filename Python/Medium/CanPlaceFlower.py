from typing import List


def canPlaceFlower(flowerbed: List[int], n: int) -> bool:

    i = 0
    while i < len(flowerbed) and n > 0:
        if flowerbed[i] == 0 and ((i == 0) or (flowerbed[i-1] == 0)) and ((i == len(flowerbed)-1 or flowerbed[i+1] == 0)): 
            n -= 1
            flowerbed[i] = 1
        i += 1
            
    return n == 0
        
    


if __name__ == '__main__':
    case1 = [1,0,0,0,1], 1
    case2 = [1,0,0,0,1], 2
    case3 = [0,0,1,0,1], 1

    print(canPlaceFlower(*case1))
    print(canPlaceFlower(*case2))
    print(canPlaceFlower(*case3))