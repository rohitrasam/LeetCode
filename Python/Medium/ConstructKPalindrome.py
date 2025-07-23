

def canConstruct(s: str, k: int) -> bool:
    if len(s) < k:
        return False
    if len(s) == k:
        return True
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    odd_count = 0
    for char in count:
        if count[char] % 2 == 1:
            odd_count += 1
    
    return odd_count <= k

if __name__ == '__main__':


    case1 = "annabelle",2
    case2 = "leetcode",3
    case3 = "true",4

    print(canConstruct(*case1))
    print(canConstruct(*case2))
    print(canConstruct(*case3))