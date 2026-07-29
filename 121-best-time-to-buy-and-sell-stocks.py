class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price=prices[0]
        max_price=0
        for current_price in prices:
            max_price=max(max_price,current_price-min_price)
            min_price=min(min_price, current_price)
        return max_price
        

        