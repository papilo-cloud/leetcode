# Given an array nums with n objects colored red, white, or blue, sort them in-place so
# that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = -1
        two_index = len(nums)
        current_index = 0

        while current_index < two_index:
            if nums[current_index] == 0:
                zero_index += 1
                nums[zero_index], nums[current_index] = nums[current_index], nums[zero_index]
                current_index += 1
            elif nums[current_index] == 2:
                two_index -= 1
                nums[two_index], nums[current_index] = nums[current_index], nums[two_index]
            else:
                current_index += 1