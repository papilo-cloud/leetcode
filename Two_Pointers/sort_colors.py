


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