"""
LeetCode Problem 217: Contains Duplicate
Approach: Frequency Counting

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counters = Counter(nums)
        for key, value in counters.items():
            if value > 1:
                return True
        return False