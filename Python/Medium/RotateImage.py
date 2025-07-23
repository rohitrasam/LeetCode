from numpy import array

def rotate(l: list[list[int]]):


    # for 3x3 matrix
    # i from 0 -> 2, j from i + 1 -> 2
            # i = 0
            # j = i+1 = 1
            # l[0, 1], l[1, 0] = l[1, 0], l[0, 1]
    
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            l[i][j], l[j][i] = l[j][i], l[i][j]
            
    # swapping cols
    for i in range(len(l)):
        for j in range(len(l)//2):
            l[i][j], l[i][len(l)-j-1] = l[i][len(l)-j-1], l[i][j]  


if __name__ == '__main__':

    arr = [
        [1, 2, 3, 4],
        [4, 5, 6, 5],
        [7, 8, 9, 10],
        [12, 13, 15, 14]
        ]

    rotate(arr)
