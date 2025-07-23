def isValid(s: str) -> bool:
    para = []
    
    for char in s:
        if char == '(' or char == '{' or char == '[':
            para.append(char)
        
        else:
            if len(para) == 0:
                return False
            if char == ')' and para[-1] == '(':
                para.pop()
            elif char == ']' and para[-1] == '[':
                para.pop()
            elif char == '}' and para[-1] == '{':
                para.pop()
            else:
                return False
    
    return not para
        


if __name__ == '__main__':
    s = input()
    print(isValid(s))