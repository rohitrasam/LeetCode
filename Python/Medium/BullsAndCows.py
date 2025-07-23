# https://leetcode.com/problems/bulls-and-cows/description/


from collections import Counter


def getHint(secret: str, guess: str) -> str:
    secret_set = Counter(secret)
    A = 0
    B = 0
    skipped = []
    for idx in range(len(guess)):
        g_item = guess[idx] 
        if g_item == secret[idx]:
            A += 1
            secret_set[g_item] -= 1
            if secret_set[g_item] == 0:
                secret_set.pop(g_item)
        else:
            skipped.append(idx)
    
    for idx in skipped:
        g_item = guess[idx] 
        if g_item in secret_set:
            B += 1
            secret_set[g_item] -= 1
            if secret_set[g_item] == 0:
                secret_set.pop(g_item)

    return f"{A}A{B}B"


if __name__ == '__main__':

    case1 = "1807", "7810"
    case2 = "1123", "0111"
    case3 = "1087", "7810"
    case4 = "1111", "0111"
    case5 = "1111", "1011"
    case6 = "1122", "1222"

    print(getHint(*case1))
    print(getHint(*case2))
    print(getHint(*case3))
    print(getHint(*case4))
    print(getHint(*case5))
    print(getHint(*case6))