from typing import List

def topKFrequent(words: List[str], k: int) -> List[str]:
    count = {}
    freq = [[] for word in words]

    for word in words:
        count[word] = 1 + count.get(word, 0)

    for key, value in count.items():
        freq[value].append(key)

    out = []
    for items in freq[::-1]:
        items.sort()
        for item in items:
            out.append(item)
            if len(out) == k:
                return out



if __name__ == '__main__':
    case1 = ["i","love","leetcode","i","love","coding"], 2
    case2 = ["the","day","is","sunny","the","the","the","sunny","is","is"], 4
    case3 = ["i","love","leetcode","i","love","coding"], 3
    print(topKFrequent(*case1))
    print(topKFrequent(*case2))
    print(topKFrequent(*case3))
