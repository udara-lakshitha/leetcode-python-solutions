"""
LeetCode Problem 268: Missing Number
Approach: Using math equation 

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)