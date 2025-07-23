def isIsomorphic(s: str, t: str) -> bool:
    table1, table2 = {}, {}
    for s1, t1 in zip(s, t):
        if s1 in table1 and table1[s1] != t1 or t1 in table2 and table2[t1] != s1:
            return False
        else:
            table1[s1] = t1
            table2[t1] = s1

    return True                


if __name__ == '__main__':
    s_ = input()
    t_ = input()
    print(isIsomorphic(s_, t_))