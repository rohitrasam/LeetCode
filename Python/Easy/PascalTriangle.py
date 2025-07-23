from math import factorial

def generate(numRows: int) -> list[list[int]]:
    pasc = [[1]]

    for i in range(1, numRows):
        row = []
        for j in range(i+1):
            num = factorial(i) / (factorial(j) * factorial(i - j))
            row.append(int(num))
        pasc.append(row)
    return pasc

if __name__ == '__main__':
    rows = int(input())

    print(generate(rows))