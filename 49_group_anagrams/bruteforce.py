"""
LeetCode Problem 49: Group Anagrams
Approach: Brute Force

Time Complexity: O(n^2 * k log k)
Space Complexity: O(n * k)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        final_arr = []
        for i in range(len(strs)):
            temp = []
            temp.append(strs[i])
            if i in seen:
                continue
            for j in range(i + 1, len(strs)):
                if j in seen:
                    continue
                if "".join(sorted(strs[i])) == "".join(sorted(strs[j])):
                    temp.append(strs[j])
                    seen.add(j)
            final_arr.append(temp)
        return final_arr