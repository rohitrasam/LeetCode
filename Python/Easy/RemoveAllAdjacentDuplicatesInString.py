# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/?envType=problem-list-v2&envId=stack

def removeDuplicates(s: str) -> str:
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)
    
    
    # stack = []

    # for char in s:
    #     if stack and stack[-1] == char:
    #         while stack and stack[-1] == char:
    #             stack.pop()
    #     else:
    #         stack.append(char)

    # return "".join(stack)



if __name__ == '__main__':

    case = "abbaca"
    print(removeDuplicates(case))
    case = "azxxzy"
    print(removeDuplicates(case))
    case = "aaaaaaaaa"
    print(removeDuplicates(case))
