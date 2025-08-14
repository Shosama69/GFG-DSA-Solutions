"""
Problem: Stock Buy and Sell
Link: https://www.geeksforgeeks.org/problems/buy-stock-2/

Description:
Given an array prices[] of length n, representing the prices of the stocks on different days.
The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed.
Here one transaction means 1 buy + 1 Sell.
If it is not possible to make a profit then return 0.


Example:
Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8

Approach:
We use one loop only for more efficient solving with the time complexity of O(n).
We set the buy as the first value from prices array and updated if we found a lower value than that.
Now we just compare some values and return the profit.
"""


class Solution:
    def maximumProfit(self, prices):
        profit = 0
        buy = prices[0]
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                if prices[i] - buy > profit:
                    profit = prices[i] - buy

        return profit

