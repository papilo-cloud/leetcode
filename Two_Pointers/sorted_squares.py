# Given an integer array nums sorted in non-decreasing order, return an array of 
# the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 

# Follow up: Squaring each element and sorting the new array is very trivial, could
# you find an O(n) solution using a different approach?


from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = 0
        result = [0]*length
        right = length - 1
        end = length - 1
        while left <= right:
            left_add = nums[left]**2
            right_add = nums[right]**2

            if left_add > right_add:
                result[end] = left_add
                left += 1
            else:
                result[end] = right_add
                right -= 1
            end -= 1
        return result
