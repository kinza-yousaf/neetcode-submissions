class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0
        l, r = 0, 1
        while r < len(prices):
            buyP = prices[l]
            minBuy = min(minBuy, buyP)
            maxP = max(maxP, prices[r] - minBuy)
            
            if prices[l] >= minBuy:
                l += 1
            
            r += 1



        return maxP



        

        
        