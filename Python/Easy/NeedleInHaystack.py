# Find the Index of the First Occurrence in a String

def strStr(haystack: str, needle: str) -> int:

    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1

if __name__ == '__main__':
    hay, needle = input().split()

    print(strStr(hay, needle))
    