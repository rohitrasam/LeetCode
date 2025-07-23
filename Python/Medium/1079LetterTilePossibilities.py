# https://leetcode.com/problems/letter-tile-possibilities/description/?envType=problem-list-v2&envId=backtracking


from collections import Counter


def numTilePossibilities(tiles: str) -> int:
    count = Counter(tiles)

    def back() -> int:
        res = 0

        for c in count:
            if count[c] > 0:
                count[c] -= 1
                res += 1
                res += back()
                count[c] += 1
        return res
    
    return back()

if __name__ == '__main__':

    case = "AAB"
    print(numTilePossibilities(case))

    case = "AAABBC"
    print(numTilePossibilities(case))

    case = "V"   
    print(numTilePossibilities(case))

