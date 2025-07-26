"""
LeetCode Problem 268: Missing Number
Approach: XOR method

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_all = 0
        xor_nums = 0
        for i in range(len(nums) + 1):
            xor_all ^= i
        for num in nums:
            xor_nums ^= num
        return xor_all ^ xor_nums