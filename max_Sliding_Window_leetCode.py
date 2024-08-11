from collections import deque
class Solution:
	def maxSlidingWindow(slef, nums: list, k: int):
		res = []
		r = l = 0
		que = deque()

		while(r<len(nums)):


			while que and nums[r] > nums[que[-1]]:
				que.pop()
			que.append(r)

			if(l> que[0]):
				que.popleft()

			if(r+1) >=k:
				res.append(nums[que[0]])
				l+=1
			r +=1




		return res

x = Solution()
print(x.maxSlidingWindow([1,2,3],2))