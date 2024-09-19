# Given the root of a binary search tree, and an integer k, return the kth
# smallest value (1-indexed) of all the values of the nodes in the tree.


# Example 1:

# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
count = 1
class Solution:
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    break
                root = stack[-1]
                res.append(root.val)
                stack.pop()
                root = root.right
        return res[k-1]