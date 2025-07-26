"""
LeetCode Problem 268: Missing Number
Approach: Brute Force

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if not i in nums:
                return i