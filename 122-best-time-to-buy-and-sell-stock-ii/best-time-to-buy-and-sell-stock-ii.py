class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits=[]
        for i in range (1,len(prices)):
            if prices[i]>prices[i-1]:
                profits.append(prices[i]-prices[i-1])
        k=sum(profits)
        
        return k