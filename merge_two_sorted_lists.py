class Solution:
    def mergeTwoLists(self, prices):
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









x = Solution()
print(x.mergeTwoLists([1,2,3,1,7]))