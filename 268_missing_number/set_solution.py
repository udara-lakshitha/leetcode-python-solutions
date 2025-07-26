"""
LeetCode Problem 268: Missing Number
Approach: Set solution

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i