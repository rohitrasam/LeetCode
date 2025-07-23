from typing import List


def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    
    for row in range(len(image)):
        image[row] = image[row][::-1]
        for idx in range(len(image[row])):
            image[row][idx] = int(not image[row][idx])
    
    return image

if __name__ == '__main__':
    case1 = [[1,1,0],[1,0,1],[0,0,0]]
    case2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

    print(flipAndInvertImage(case1))
    print(flipAndInvertImage(case2))