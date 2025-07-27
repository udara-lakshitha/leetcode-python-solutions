"""
LeetCode Problem 217: Contains Duplicate
Approach: Set Insertion + Early Exit

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False