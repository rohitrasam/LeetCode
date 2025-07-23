from typing import List

def compareVersion(version1: str, version2: str) -> int:
    version1 = version1.split(".")
    version2 = version2.split(".")
    
    v1 = v2 = 0
    while v1 < len(version1) or v2 < len(version2):
        n1 = 0 if v1 >= len(version1) else int(version1[v1])
        n2 = 0 if v2 >= len(version2) else int(version2[v2])
        if n1 < n2:
            return -1
        elif n2 <  n1:
            return 1
        v1, v2 = v1 + 1, v2 + 1
    
    return 0

if __name__ == '__main__':

    case1 = "1.2", "1.10"
    case2 = "1.01", "1.001"
    case3 = "1.0", "1.0.0.0"

    print(compareVersion(*case1))
    print(compareVersion(*case2))
    print(compareVersion(*case3))