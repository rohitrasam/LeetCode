def isPalindrome(string: str) -> bool:

    string = "".join(filter(str.isalnum, string)).lower()
    print(string)

    # for alpha in string:
    #         if not alpha.isalnum():
    #             string = string.replace(alpha, '')
    # string = string.lower()

    return string == string[::-1]

if __name__ == '__main__':

    s = input()

    print(isPalindrome(s))

    