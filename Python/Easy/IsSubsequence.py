


def isSubsequence(s: str, t: str):
    
    if len(s) == 0:
        return True
    elif len(t) == 0 or len(s) > len(t):
        return False

    s_idx = 0
    for ch in t:
        if ch == s[s_idx]:
            s_idx += 1
            if s_idx == len(s):
                return True
        
    return False
    # t_idx = 0
    # while s_idx < len(s) and t_idx < len(t):
    #     if t[t_idx] == s[s_idx]:
    #         s_idx += 1
    #         t_idx += 1
    #     else:
    #         t_idx += 1
    
    # return s_idx == len(s)

if __name__ == '__main__':

    string = input()
    tring = input()

    print(isSubsequence(string, tring))