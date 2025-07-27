"""
LeetCode Problem 121: Best Time to Buy and Sell Stock
Approach: two pointers

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if min_price < price:
                max_profit = max(max_profit, (price - min_price))
            else:
                min_price = price
        return max_profit