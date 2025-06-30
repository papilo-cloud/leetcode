# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).


# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100


from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(root1, root2):
            if (not root1) and (not root2):
                return True
            if (not root1) or (not root2):
                return False
            if root1.val != root2.val:
                return False
            return (symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left))

        return symmetric(root, root)