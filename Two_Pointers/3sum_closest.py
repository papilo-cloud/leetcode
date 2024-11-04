# Given an integer array nums of length n and an integer target, find three 
# integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        min_diff = float('inf')
        nums.sort()
        res = 0

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                diff = abs(summ - target)
                if diff < min_diff:
                    min_diff = diff
                    res = summ
                if summ > target:
                    r -= 1
                else:
                    l += 1
        return res