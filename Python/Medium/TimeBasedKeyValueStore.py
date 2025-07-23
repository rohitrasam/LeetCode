# https://leetcode.com/problems/time-based-key-value-store/

from typing import Dict, Tuple


class TimeMap:

    def __init__(self):
        self.hash: Dict[str, Tuple[str, int]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:        
        val = self.hash.setdefault(key, [])
        val.append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        prev, vals = "", self.hash.get(key, [])

        l, r = 0, len(vals)-1

        while l <= r:
            mid = (l + r) // 2
            if timestamp < vals[mid][1]:
                r = mid - 1
            else:
                prev = vals[mid][0]
                l = mid + 1            
        return prev
        
    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
if __name__ == '__main__':
    obj = TimeMap()
    obj.set("love", "high", 10)
    obj.set("love", "low", 20)
    print(obj.get("love", 5))
    print(obj.get("love", 10))
    print(obj.get("love", 15))
    print(obj.get("love", 20))
    print(obj.get("love", 25))