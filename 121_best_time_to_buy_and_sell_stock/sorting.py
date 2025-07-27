"""
LeetCode Problem 121: Best Time to Buy and Sell Stock
Approach: Sorting (worst than brute force)

Time Complexity: O(n^2 log n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            max_sell = max(sorted(prices[i + 1:]))
            if prices[i] < max_sell:
                max_profit = max(max_profit, (max_sell - prices[i]))
        return max_profit