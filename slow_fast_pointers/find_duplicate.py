# Given an array of integers nums containing n + 1 integers where each integer is in 
# the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant
# extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

# Follow up:

# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?


from bisect import bisect_left

# Solution #1
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        def is_above_x(x):
            count = sum(num <= x for num in nums)
            return count > x
        
        duplicate = bisect_left(range(len(nums)), True, key=is_above_x)
        return duplicate


# Solution #1
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow