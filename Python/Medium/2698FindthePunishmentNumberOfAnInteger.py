# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/?envType=problem-list-v2&envId=backtracking



def punishmentNumber(n: int) -> int:
    
    res = 0

    def partition(idx: int, cur: int, target: int, string: str) -> bool:
        if idx == len(string) and cur == target:
            return True
        
        for j in range(idx, len(string)):
            
            if partition(j + 1, cur + int(string[idx:j+1]), target, string):
                return True
        
        return False

    for i in range(1, n + 1):
        if partition(0, 0, i, str(i*i)):
            res += i * i
        
    return res


if __name__ == '__main__':

    case = 5
    print(punishmentNumber(case))
    case = 10
    print(punishmentNumber(case))
    case = 37
    print(punishmentNumber(case))
    case = 100
    print(punishmentNumber(case))
