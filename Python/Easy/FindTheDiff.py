def findDiff(s: str, t: str):
    
    s_list = list(s)
    for ch in t:
        if ch not in s_list:
            return ch
        s_list.remove(ch)


if __name__ == '__main__':

    s = input()
    t = input()

    print(findDiff(s, t))