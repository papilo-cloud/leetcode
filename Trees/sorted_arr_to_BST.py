# Given the head of a singly linked list where elements are sorted in ascending order,
# convert it to a 
# height-balanced
#  binary search tree.

 

# Example 1:


# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height
# balanced BST.
# Example 2:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in head is in the range [0, 2 * 104].
# -105 <= Node.val <= 105


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: # type: ignore
        def convert(l, r):
            if l > r:
                return None
            mid = (l + r)//2
            l_tr = convert(l, mid - 1)
            r_tr = convert(mid + 1, r)

            return TreeNode(nums[mid], l_tr, r_tr)
        return convert(0, len(nums) - 1)