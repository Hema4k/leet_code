class Solution:
	def maxArea(self, bars: list[int]):

		i = 0 
		j = len(bars)-1

		maxArea = 0

		while(i < j):
			curArea = (j - i) * min(bars[i],bars[j])
			maxArea = max(maxArea,curArea)

			if(bars[i] > bars[j]):
				j-=1
			elif(bars[i] <= bars[j]):
				i+=1


		return maxArea

# a  problem wih two pointers where we look for heighest bars
# and calculate the biggest area possible with one poitners approaching
# from the left and other from the right, and if a bar is lower in height
# than the other we just shift to the next bar, basically having the highest bar
# with the furthest distance possible from each other


			



