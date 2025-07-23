def countBits(n: int) -> list[int]:
    ans = []
    for i in range(n+1):
        ans.append(sum(list(map(int, bin(i)[2:]))))
    
    return ans



if __name__ == '__main__':
    num = int(input())
    print(countBits(num))