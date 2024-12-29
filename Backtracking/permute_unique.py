# Given a collection of numbers, nums, that might contain duplicates, 
# return all possible unique permutations in any order.

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

# Constraints:

# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10


from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        chk = [False]*len(nums)
        def dfs(path):
            if len(path) == len(nums):
                return ans.append(path.copy())
            for i, n in enumerate(nums):
                if chk[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not chk[i-1]:
                    continue
                chk[i] = True
                path.append(n)
                dfs(path)
                path.pop()
                chk[i] = False
        nums.sort()
        dfs([])
        return ans