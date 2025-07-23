def wordPattern(pattern: str, s: str) -> bool:
    # if len(pattern) != len(s):
    #     return False
    hashmap = {}
    s = s.split()

    for word1, word2 in zip(pattern, s):
        if word1 in hashmap and hashmap[word1] != word2:
            return False
        else:
            hashmap[word1] = word2

        if len(set(hashmap.keys())) != len(set(hashmap.values())):
            return False
    return True
            


if __name__ == '__main__':
    pat = input()
    st = input()
    
    print(wordPattern(pat, st))