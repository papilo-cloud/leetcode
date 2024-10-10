# Given the root of a binary tree, invert the tree, and return its root.


# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        stk = []
        stk.append(root)
        while stk:
            node = stk.pop()
            s = node.left
            node.left = node.right
            node.right = s
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        return root