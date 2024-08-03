class Solution:
    def mxProfit(self, prices):
    	i = 0
    	j = 1
    	maxPrice = 0
    	while(j < len(prices)):
    		if( prices[i]< prices[j]):
    			currentPrice = prices[j] - prices[i]
    			maxPrice = max(maxPrice, currentPrice)

    		else:
    			i = j
    		j+=1

    	return maxPrice

