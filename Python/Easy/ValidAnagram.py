def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    visited = {}

    for char in s:
        if char in visited:
            visited[char] += 1
        else:
            visited[char] = 1
    
    for char in t:
        if char in visited:
            if visited[char] > 0:
                visited[char] -= 1
                if visited[char] == 0:
                    visited.pop(char)
    
    return len(visited) == 0





if __name__ == '__main__':
    st = input()
    ts = input()

    print(isAnagram(st, ts))