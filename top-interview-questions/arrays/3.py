# Rotate Array
# ------------
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
# Example:
#   Input: nums = [1,2,3,4,5,6,7], k = 3
#   Output: [5,6,7,1,2,3,4]
#   Explanation:
#       rotate 1 steps to the right: [7,1,2,3,4,5,6]
#       rotate 2 steps to the right: [6,7,1,2,3,4,5]
#       rotate 3 steps to the right: [5,6,7,1,2,3,4]
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]

if __name__ == '__main__':
    s = Solution()
    n_list = [1,2]
    s.rotate(n_list, 3)
    print(n_list)