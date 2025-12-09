from typing import List
from collections import Counter

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.count = size
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        
        return self.find(self.parent[i])
    
    def unite(self, i, j):
        iRep = self.find(i)
        jRep = self.find(j) 
        if iRep != jRep:
            self.count -= 1
        self.parent[iRep] = jRep

    def get_component_sizes(self) -> List[int]:

        rootList = [self.find(i) for i in range(len(self.parent))]

        counts = Counter(rootList)

        return list(counts.values())
    
    def get_component_count(self) -> int:
        return self.count