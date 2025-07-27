"""
LeetCode Problem 217: Contains Duplicate
Approach: Sorting and Adjacent Check

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False