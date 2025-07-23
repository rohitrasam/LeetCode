

# import time

# a = list(range(1000))

# t1 = time.perf_counter()
# for i in range(1000):
#     a[i] **= 2
# t2 = time.perf_counter()

# print(t2 - t1)

# a = list(range(1000))

# t1 = time.perf_counter()
# a = list(map(lambda x: x**2, a))
# t2 = time.perf_counter()
# print(t2 - t1)


    

# l = None
# with open(r'D:\Python Programs\LeetCode\Easy\text.txt', 'r') as f:
#     l = f.read()
    
#     l = [each.split() for each in l.split("\n")]

#     l = list(map(lambda x: (x[0], float(x[1]), x[2]), l))


# with open(r'D:\Python Programs\LeetCode\Easy\text.txt', 'w') as f:
#     for i, j, k in l:
#         f.write(f"('{i}', {j}, '{k}'),\n")

# import cmath

# a = complex(2, 3)
# comp = lambda x: complex(2, x)

# a = 3
# print(comp(a))[]


# roots_func = lambda a, b, c: (((-b) + (b**2-4*a*c)**0.5)/(2*a), ((-b) - (b**2-4*a*c)**0.5)/(2*a))


# while True:
#     a, b, c = map(float, input("Enter values of a, b, c: ").split())
#     roots = roots_func(a, b, c) 
#     print(f"Roots are {roots[0]:.3f}, {roots[1]:.3f}")


# from math import comb

# def bion(a, b, n):
#     total = 0
#     for r in range(n+1):
#         total += comb(n, r) * a**(n-r) * b**r

#     return total

# print(bion(2, 5**0.5, 5) * bion(2, -5**0.5, 5))



# f = {"name": "Rohit", "age": 24}
# print(f["name"][2])
# lst1: list[int] = ["a", 1, 2]

# print(lst1)

# def append(num, l=[]):
#     l.append(num)
#     return l

# l1 = append(1)
# print(l1)
# l2 = append(2)
# print(l2)


# graph = {0: [2,3], 1:[0, 1, 2], 2: [0, 1, 4], 3: [1, 4], 4: [3, 4]}

# visited = set()
# q = []

# q.append(0)
# visited.add(0)

# while q:
#     node = q.pop(0)
#     print(f"Current node: {node}")
#     for child in graph[node]:
#         if child not in visited:
#             q.append(child)
#             visited.add(child)

# def temp(a):
#     return 0 if a == 0 else ("Pos" if a > 0 else "Neg")

# print(temp(0))
# print(temp(1))
# print(temp(-1))



# def quickSort(nums: list[int], left: int, right: int) -> None:
#     if left < right:
#         pivot = partition(nums, left, right)
#         quickSort(nums, left, pivot-1)
#         quickSort(nums, pivot + 1, right)


# def partition(nums: list[int], left: int, right: int) -> int:
#     i = left
#     j = right - 1

#     pivot = nums[right]

#     while i < j:
#         while i < right and nums[i] < pivot:
#             i += 1

#         while j > left and nums[j] >= pivot:
#             j-= 1
        

#         if i < j:
#             nums[i], nums[j] = nums[j], nums[i]
        
#     if nums[i] > pivot:
#         nums[i], nums[right] = nums[right], nums[i]
        
#     return i
    

# l = [5,4,10,21,2,-1,0]
# quickSort(l, 0, len(l)-1)
# print(l)

    

# def move_zeros(nums: list[int]):

#     l = 0
#     r = len(nums) - 1

#     while l < r:
#         if nums[l] == 0:
#             nums.append(nums[l])
#             nums.pop(l)
#             r -= 1
#         if nums[l] != 0:
#             l += 1
        
# a = [0, 0, 1, 3, 0, 33, 12, 0, 10, 0]
# move_zeros(a)

# def find_one(nums: list[int]) -> int:
#     ans = nums[0]
#     for num in nums[1:]:
#         ans ^= num
    
#     return ans

# a = [4, 1, 2, 1, 2, 4, 3]
# print(find_one(a))

# import random

# for j in range(4):
#     num = []
#     for i in range(100):
#         num.append(random.randint(-100, 100))
#     print(*num, end="\n=====\n")

# def pre_req(x: int, yn: str) -> bool:
#     res = False
#     def helper(i: int, count: int) -> None:
#         if i >=len(yn) and x != count:
#             res = False
#             return 
#         if i >= len(yn) and x == count:
#             res = True
#             return 
        
#         if (not yn[i].isdigit()) or (i > 0 and yn[i].isdigit() and yn[i-1].isdigit()):
#             helper(i+1, count)
#         if yn[i].isdigit():
#             helper(i+1, count+1)
#     helper(0, 0)
#     return res




# i = 0
# while i < 3:
#     print(i)
#     if i == 2:
#         break
#     i += 1 
# else:
#     print(0)  
# print([[i+j for i in "abc"] for j in "def"])



# def printAllPaths(n: int, m: int) -> list[str]:
#     paths: list[str] = []

#     def dfs(prev_row: int, row: int, prev_col: int, col: int, path: list[str]) -> None:

#         if row >= n and col >= m:
#             paths.append(path)
#             return
#         if row < n and col < m:
#             if row != prev_row and col == prev_col:
#                 path.append("v")
#             if row == prev_row and col != prev_col:
#                 path.append("h")
#             if row != prev_row and col != prev_col:
#                 path.append("d")
#         else:
#             return
        
#         dfs(row, row + 1, col, col, path)
#         dfs(row, row, col, col + 1, path)
#         dfs(row, row+1, col, col + 1, path)
    
#     dfs(0, 0, 0, 0, [])
#     return paths


# if __name__ == '__main__':

#     for i in range(2, 6):
#         for j in range(2, 6):
#             print(printAllPaths(i, j))

# graph = {0: [1,2,3], 1:[0, 2], 2: [0, 1, 4], 3: [1, 4], 4: [2,3]}

# def dfs():
#     visited: set[int] = set()
#     stack: list[int] = []
#     stack.append(0)
#     visited.add(0)

#     while stack:
#         node = stack.pop()
#         print(node)
        
#         for child in graph[node]:
#             if child not in visited:
#                 stack.append(child)
#                 visited.add(child)

# dfs()

# from dataclasses import dataclass


# @dataclass
# class P:    

#     __slots__ = "name"
#     name: str
#     age: int


# p = P("Rohit", 26)
# p.date = "29/02/2011"
# print(p)

# from abc import ABC, abstractmethod


# class Phone(ABC):

#     def __init__(self, model: str):
#         self.model = model

#     @abstractmethod
#     def call(self, name: str):
#         ...

# class Apple(Phone):

#     def __init__(self, model: str):
#         super().__init__(model)
    
#     def call(self, name: str):
#         print(f"Calling {name}")
        

# apple = Apple("iPhone 12")
# apple.call("Ameya")

# class Person:

#     def hello(self):
#         print(type(self))
#         print(f"{self.name} says hello")

# class Student(Person):

#     name = "Rohit"

# p = Person()
# st = Student()
# st.hello()  # works!
# p.hello()   # gives an error


# from typing import Dict, List, Tuple


# def temp(i: int, *args: Tuple[int, ...], **kwargs: Dict[str, int]):
#     args: List[int] = list(args)
#     kwargs: Dict[str, int] = dict(kwargs)
#     print(i, args[0], kwargs)


# temp(1, 0, 1, 2, 3, a=2, b=4)
a = list(range(100))
print(a)