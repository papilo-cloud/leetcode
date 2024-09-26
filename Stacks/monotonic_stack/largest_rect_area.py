# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Example 1:

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:

# Input: heights = [2,4]
# Output: 4
 
# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

class Solution:
    def largestRectangleArea(self, heights) -> int:
        
        max_area = 0
        h = len(heights)
        stack = []
        i = 0

        while i <= h:
            if i == h:
                max_h = 0
            else:
                max_h = heights[i]
            
            if (not stack) or (max_h >= heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                max_area = max(max_area, heights[top]*((i - stack[-1] - 1) if stack else i))
        return max_area