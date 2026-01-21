class SegmentTree:
    def __init__(self, total: int, L: int, R: int):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R
    
    # O(n)
    @staticmethod
    def build(nums: list, L: int, R: int) -> SegmentTree:
        if L == R:
            return SegmentTree(nums[L], L, R)
        
        mid = (L + R) // 2

        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, mid)
        root.right = SegmentTree.build(nums, mid + 1, R)
        root.sum = root.left.sum + root.right.sum

        return root

    # O(log n)
    def update(self, index: int, val: int):
        if self.L == self.R:
            self.sum = val
            return
        
        mid = (self.L + self.R)//2

        if index <= mid:
            self.left.update(index, val)
        else:
            self.right.update(index, val)

        self.sum = self.left.sum + self.right.sum

    # O(log n)
    def rangeQuery(self, L: int, R: int) -> int:
        if self.L == L and self.R == R:
            return self.sum
        
        mid = (self.L + self.R)//2

        # Entire range lies in left subtree
        if R <= mid:
            return self.left.rangeQuery(L, R)
        # Entire range lies in right subtree
        elif L > mid:
            return self.right.rangeQuery(L, R)
        # Range spans both subtrees
        else:
            return self.left.rangeQuery(L, mid) + self.right.rangeQuery(mid + 1, R)