def reverseStr(s: str, k: int) -> str:
    if len(s) < k:
        return ''.join(list(s)[::-1])

    s = list(s)
    l = 0
    r = k - 1
    i = 1
    
    while l < len(s) :
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        l = i*2*k
        r = (l + k - 1) if l + k -1 < len(s) else len(s)-1
        i += 1

    return ''.join(s)
    

if __name__ == '__main__':
    case1 = "abcdefg", 2
    case2 = "abcd", 2
    case3 = "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39

    # print(reverseStr(*case1))
    # print(reverseStr(*case2))
    print(reverseStr(*case3))
