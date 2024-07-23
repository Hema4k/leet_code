class Solution:
	def longestConsecutive(self, nums: list[int]):
		s = set(nums)
		longest = 0
		for num in nums:
			if(num - 1 not in s):
				length = 1

				while(num + 1 in s):
					length +=1
					num+=1
				longest = max(longest, length)
		return longest





x = Solution()
print(x.longestConsecutive([0, 1,2,3,100,101,102,103,104,-10,-9,-8,-7,-6,-5,-4]))