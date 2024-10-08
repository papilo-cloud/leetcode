# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
 

# Example 1:
# Input: nums = [3,2,3]
# Output: [3]

# Example 2:
# Input: nums = [1]
# Output: [1]

# Example 3:
# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count1 = 0
        count2 = 0
        major_elem1 = None
        major_elem2 = None
        for i in range(len(nums)):

            if nums[i] == major_elem1:
                count1 += 1
            elif nums[i] == major_elem2:
                count2 += 1
            elif count1 == 0:
                major_elem1 = nums[i]
                count1 = 1
            elif count2 == 0:
                major_elem2 = nums[i]
                count2 = 1
            
            else:
                count1 -= 1
                count2 -= 1
        return [x for x in (major_elem1, major_elem2) if nums.count(x) > len(nums)//3]