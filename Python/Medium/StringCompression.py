# https://leetcode.com/problems/string-compression/description/?envType=problem-list-v2&envId=two-pointers


from typing import List


def compress(chars: List[str]) -> int:
    i, j = 0, 1
    count = 0
    while j < len(chars):
        if chars[j] == chars[i]:
            count += 1
            j += 1
        if j >= len(chars) or chars[j] != chars[i]:
            count += 1
            if count > 1:
                jump = 0
                while count != 0:
                    rem = count % 10
                    count //= 10
                    chars.insert(i+1, str(rem))
                    jump += 1
                    j += 1
                i += jump+1
                while i != j:
                    chars.pop(i)
                    j -= 1
                j = i + 1
            else:
                count = 0
                i += 1
                j += 1
    
    return len(chars)


if __name__ == '__main__':

    case = ["a","a","b","b","c","c","c"]
    print(compress(case))
    case = ["a"]
    print(compress(case))
    case = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(compress(case))
    case = [".", ".", ".", "b","b","b","b","b","b","b","b","b","b","b","b", "1", "1"]
    print(compress(case))