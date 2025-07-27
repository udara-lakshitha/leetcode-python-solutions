"""
LeetCode Problem 217: Contains Duplicate
Approach: Set Length Comparison

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)