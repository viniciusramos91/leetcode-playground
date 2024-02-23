# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same. Then return the number of
# unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#   - Change the array nums such that the first k elements of nums contain the unique elements in the order they were
#     present in nums initially. The remaining elements of nums are not important as well as the size of nums.
#   - Return k.
# Example:
#   Input: nums = [1,1,2]
#   Output: 2, nums = [1,2]
#   Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
#   It does not matter what you leave beyond the returned k (hence they are underscores).

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        control = nums[0]
        for num in nums[1:]:
            if num == control:
                nums.remove(num)
            control = num

        return len(set(nums))

if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,2,3,4,5,5,6]
    s.removeDuplicates(nums)