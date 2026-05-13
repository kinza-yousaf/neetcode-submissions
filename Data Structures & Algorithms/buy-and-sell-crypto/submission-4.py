class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0
        for sellPrice in prices:
            minBuy = min(minBuy, sellPrice)
            maxP = max(sellPrice - minBuy, maxP)



        return maxP



        

        
        