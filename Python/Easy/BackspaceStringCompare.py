
def backspaceCompare(s: str, t: str) -> bool:
    
    def removeBackspace(string: str):
        stack = []
        for char in string:
            if stack and char == "#":
                stack.pop()
            elif char != "#":
                stack.append(char)
        return stack

    return removeBackspace(s) == removeBackspace(t)

if __name__ == '__main__':
    case1 = "ab#c", "ad#c"
    case2 = "ab##", "c#d#"
    case3 = "a#c", "b"
    case4 = "xywrrmp", "xywrrmu#p"

    print(backspaceCompare(*case1))
    print(backspaceCompare(*case2))
    print(backspaceCompare(*case3))
    print(backspaceCompare(*case4))