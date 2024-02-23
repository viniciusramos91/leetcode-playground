# Contains Duplicate
# ------------------
# Given an integer array nums, return true if any value appears at least twice in the array, and
# return false if every element is distinct.
# Example:
#   Input: nums = [1,1,1,3,3,4,3,2,4,2]
#   Output: true
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate(nums=[]))