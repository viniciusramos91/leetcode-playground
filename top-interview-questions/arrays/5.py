# Single Number
# -------------
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
# Example:
#   Input: nums = [2,2,1]
#   Output: 1
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            control = nums[i]
            ans = ans ^ control
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))