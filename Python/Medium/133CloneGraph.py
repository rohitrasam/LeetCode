# https://leetcode.com/problems/clone-graph/?envType=problem-list-v2&envId=graph

from typing import Deque, Dict, List, Optional, Set
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Optional[Node]) -> Optional[Node]:
    
    if not node:
        return None

    q: Deque[Node] = deque(node)
    clone: Dict[str, Node] = {}
    q.append(node)
    clone[node.val] = Node(node.val)

    while q:
        curr = q.popleft()

        new_node = clone.get(curr.val)   
        if not new_node:
            new_node = Node(curr.val)

        for neighbour in curr.neighbors:
            new_neighbour = clone.get(neighbour.val)
            if not new_neighbour:
                new_neighbour = Node(neighbour.val)
            new_node.neighbors.append(new_neighbour)

            if neighbour.val not in clone:
                q.append(neighbour)
                clone[neighbour.val] = new_neighbour
        
    return clone[node.val]



