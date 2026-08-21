class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for current_price in prices:
            if current_price<min_price:
                min_price=current_price

            if (current_price - min_price) > max_profit:
                max_profit = current_price - min_price

        return max_profit
