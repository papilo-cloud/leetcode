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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]: # type: ignore
        def mid_node(head):
            slow = head
            fast = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return slow

        if not head:
            return None
        if not head.next:
            return TreeNode(head.val) # type: ignore
        
        mid = mid_node(head)
        root = TreeNode(mid.val) # type: ignore
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
