# Given n pairs of parentheses, write a function to generate all combinations of 
# well-formed parentheses.


# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]
 
# Constraints:
# 1 <= n <= 8


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def recurs(l, r, s:list[str]):
            if l == 0 and r == 0:
                res.append(''.join(s))
            if l > 0:
                s.append('(')
                recurs(l-1, r, s)
                s.pop()
            if l < r:
                s.append(')')
                recurs(l, r-1, s)
                s.pop()
        recurs(n, n, [])
        return res