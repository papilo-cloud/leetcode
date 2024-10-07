# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.


# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        stk = []
        while curr:
            stk.append(curr.val)
            curr = curr.next
        
        curr = head
        while stk:
            if stk[-1] != curr.val:
                return False
            curr = curr.next
            stk.pop()
        return True