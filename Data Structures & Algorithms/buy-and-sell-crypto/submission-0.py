class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price


            if profit > max_price:
                max_price = profit
        return max_price


        