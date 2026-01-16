class UnionFind:
    def __init__(self):
        self.par = {}
        self.rank = {}
    
    def find(self, node: int) -> None:
        p = self.par[node] 

        while p != self.par[node]:
            # path compression: make the grandparent the parent
            self.par[p] == self.par[self.par[node]]
            p = self.par[p]

        return p
    
    def union(self, node1, node2) -> bool:
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False

        if self.rank[node1] > self.rank[node2]:
            # if node 1 is bigger, make it the parent
            self.par[node2] = node1
        elif self.rank[node1] < self.rank[node2]:
            self.par[node1] = node2
        else:
            self.par[node1] = node2
            self.rank[node2] += 1
        
        return True