class UnionFind:
    def __init__(self):
        # genric union find structure
        # need to initialize par and rank
        self.par = {}
        self.rank = {}
    
    def find(self, node: int) -> None:
        parent = self.par[node]
        while parent != self.par[parent]:
            # path compression: make the grandparent the parent
            self.par[parent] == self.par[self.par[parent]]
            parent = self.par[parent]

        return parent
    
    def union(self, node1, node2) -> bool:
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False

        if self.rank[parent1] > self.rank[parent2]:
            # if node 1 is bigger, make it the parent
            self.par[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.par[parent1] = parent2
        else:
            self.par[parent1] = parent2
            self.rank[node2] += 1
        
        return True