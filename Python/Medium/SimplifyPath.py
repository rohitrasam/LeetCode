

def simplifyPath(path: str) -> str:
    # stack = []
    # path = path.split("/")

    # for _file in path:
    #     if not _file or _file == ".":
    #         continue
    #     if _file == ".." and stack:
    #         stack.pop()
    #     elif _file != '..':
    #         stack.append(_file)

    # return "/" + "/".join(stack)

    path_stack = []
    path_split = path.split('/')
    path_split = [p for p in path_split if p]

    for p in path_split:
        if p == '..':
            if path_stack:
                path_stack.pop()
        elif p != '.':
            path_stack.append(p)
    
    return "/" + "/".join(path_stack)


if __name__ == '__main__':

    case1 = "/home/"
    case2 = "/home//foo/"
    case3 = "/home/user/Documents/../Pictures"
    case4 = "/../"
    case5 = "/.../a/../b/c/../d/./"
    case6 = "/a/../../b/../c//.//"
    case7 = "/d/a/../../b/../c//.//"

    for case in (case1, case2, case3, case4, case5):
        print(simplifyPath(case))
    print(simplifyPath(case6))
    print(simplifyPath(case7))