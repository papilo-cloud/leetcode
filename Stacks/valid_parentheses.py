# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if self.is_opening_brace(char):
                stack.append(char)
            elif self.is_closing_brace(char):
                if not stack:
                    return False
                popped_opening_brace = stack.pop()
            
                if self.is_not_a_match(popped_opening_brace, char):
                    return False
            
        if stack:
            return False 
        return True       
    
    def is_opening_brace(self, char):
        return (char in ["(", "[", "{"])
    
    def is_closing_brace(self, char):
        return (char in [")", "]", "}"])
    
    def is_not_a_match(self, opening_brace, closing_brace):
        tags = {'(': ')', '[': ']', '{':'}'}
        return tags[opening_brace] != closing_brace