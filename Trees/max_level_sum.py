# Given the root of a binary tree, the level of its root is 1, the level of its
# children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level 
# x is maximal.


# Example 1:
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# Example 2:
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        res = []
        if not root:
            return res
        q = []
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)

                if node.left:
                   q.append(node.left)
                if node.right:
                   q.append(node.right)
            res.append(sum(level))

        maxx = res[0]
        fl = res[0]
        for i in range(1, len(res)):
            if res[i] > fl:
                fl = res[i]
                maxx = i +1
        return maxx