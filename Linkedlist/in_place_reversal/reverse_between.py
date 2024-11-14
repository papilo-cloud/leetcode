# Given the head of a singly linked list and two integers left and
# right where left <= right, reverse the nodes of the list from 
# position left to position right, and return the reversed list.

# Example 1:

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]
 
# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
 

class Solution:
    def reverse(self, head):
        current = head
        previous = None
        while current:
            new_node = current.next
            current.next = previous
            
            previous = current
            current = new_node
        return previous 
    def reverseBetween(self, head, left: int, right: int):
        if left == right:
            return head
        rev = None 
        rev_prev = None 
        revend = None 
        revend_next = None 
        
        current = head
        i = 1
        while current and (i <= right):
            if i < left:
                rev_prev = current
            if i == left:
                rev = current
            if i == (right):
                revend = current
                revend_next = current.next
            current = current.next
            i += 1
        
        if revend:
            revend.next = None
        revend = self.reverse(rev)
        
        if rev_prev:
            rev_prev.next = revend
        else:
            head = revend
            
        if rev:
            rev.next = revend_next
        return head