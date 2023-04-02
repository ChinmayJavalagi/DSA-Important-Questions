""" Maintain a maxProfit and a minPrice variables, iterate, keep track of min value and max profit untill that point of time."""
# TC - O(N)

class Solution(object):
    def maxProfit(self, prices):
        maxProfit, minPrice = 0, prices[0]
        for i in range(1,len(prices)):
            maxProfit = max(maxi, prices[i] - mini)
            minPrice = min(mini, prices[i])
        return maxi        
