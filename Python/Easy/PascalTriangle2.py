from math import factorial


def getRow(rowIndex: int) -> int:
    row = [1]
    for j in range(1, rowIndex+1):
        num = row[j-1] * ((rowIndex - (j - 1)) / j) 
        # num = factorial(rowIndex) / (factorial(j) * factorial(rowIndex - j))
        row.append(int(num))

    return row

if __name__ == '__main__':
    idx = int(input())

    print(getRow(idx))