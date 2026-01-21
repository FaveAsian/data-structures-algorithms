class TreeNode:
    def __init__(self, value: int, left:TreeNode = None, right: TreeNode = None):
        self.value = value
        self.left = left
        self.right = right
class DFS:
    # time and space complexity: O(n)
    # specifically space complexity is O(h) where h is the height of the tree
    def inorder_dfs(self, root: TreeNode):
        stack = []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                print(curr.value)  # Process the node
                curr = curr.right

    # time and space complexity: O(n)
    # specifically space complexity is O(h) where h is the height of the tree
    def preorder_dfs(self, root: TreeNode):
        stack = []
        curr = root

        while curr or stack:
            if curr:
                print(curr.value)  # Process the node
                if curr.right:
                    stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

    # time and space complexity: O(n)
    # specifically space complexity is O(h) where h is the height of the tree
    def postorder_dfs(self, root: TreeNode):
        stack = [root]
        visited = [False] # a stack

        while stack:
            curr, visited = stack.pop(), visited.pop()
            if curr:
                if visited:
                    print(curr.value)  # Process the node
                else:
                    # add right child first so that left child is processed first
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)   
