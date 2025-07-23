# https://leetcode.com/problems/longest-palindrome/?envType=problem-list-v2&envId=hash-table

from collections import Counter


def longestPalindrome(s: str) -> int:
    """ My solution """
    if len(s) == 1:
        return 1
    
    counter = Counter(s)

    longest = 0
    curr = 0
    odd = 0


    for char in counter:
        curr += counter[char]
        if curr % 2 == 0 and counter[char] % 2 != 0 and odd == 1:
            curr -= 1
            continue

        if counter[char] % 2 != 0:
            odd += 1

        if curr % 2 == 0:
            if curr > longest:
                longest = curr
        else:
            if odd == 1 and curr > longest:
                longest = curr

    return max(curr, longest)


if __name__ == '__main__':


    case = "abccccdd"
    # print(longestPalindrome(case))
    case = "ccccdd"
    print(longestPalindrome(case))
    case = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    print(longestPalindrome(case))
    case = "a"
    print(longestPalindrome(case))