"""
LeetCode Problem 242: Valid Anagram
Approach: Sorting approach

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute force approach
        list_s = list(s)
        list_t = list(t)
        for i in range(len(list_s)):
            is_found = False
            for j in range(len(list_t)):
                if list_t[j] == list_s[i]:
                    list_t[j] = None
                    is_found = True
                    break
            if not is_found:
                return False
        for letter in list_t:
            if letter:
                return False
        return True
