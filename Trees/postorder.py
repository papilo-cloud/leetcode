# Given the root of a binary tree, return the postorder traversal
# of its nodes' values.


# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,6,7,5,2,9,8,3,1]


# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]

 

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return
        visited = {}
        s = []
        res = []
        node = root
        while node or s:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                if node.right and not node.right in visited:
                    s.append(node)
                    node = node.right
                else:
                    visited[node] = 1
                    res.append(node.val)
                    node = None
        return res