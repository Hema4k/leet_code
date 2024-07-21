class Solution:
	def productOfAnArrayExceptItself(self, nums:list[int]) -> list:
		result = [1]*len(nums)
		
		for i in range(len(nums)):
			if(i!=0):# leave result[0] =1 as it as
				result[i] = result[i-1] * nums[i-1]
		temp = 1
		for j in range(len(nums)-1,-1,-1):
			if(j!=len(nums)-1):# leave result[-1] as it as
				temp = temp *nums[j+1]
				result[j]*=temp
				 
		return result
