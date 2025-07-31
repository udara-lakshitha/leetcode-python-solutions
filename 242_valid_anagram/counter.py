"""
LeetCode Problem 242: Valid Anagram
Approach: Frequency counter

Time Complexity: O(n)
Space Complexity: O(1)
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Hashmap solution
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t
