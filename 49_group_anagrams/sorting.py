"""
LeetCode Problem 49: Group Anagrams
Approach: Categorized by sorted string

Time Complexity: O(n * k log k)
Space Complexity: O(n * k)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        for word in strs:
            sorted_str = "".join(sorted(word))
            if not sorted_str in str_map:
                str_map[sorted_str] = [word]
            else:
                str_map[sorted_str].append(word)
        final_arr = []
        for value in str_map.values():
            final_arr.append(value)
        return final_arr