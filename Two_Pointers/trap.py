# Given n non-negative integers representing an elevation map where the width of each bar 
# is 1, compute how much water it can trap after raining.


# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
# In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


class Solution:
    def trap(self, height: list[int]) -> int:
        left = 1
        right = len(height) - 2

        left_max = height[left - 1]
        right_max = height[right + 1]
        result = 0
        while left <= right:
            if right_max <= left_max:
                result += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1
            else:
               result += max(0, left_max - height[left])
               left_max = max(left_max, height[left])
               left += 1
        return result