class Solution():
	def dailyTemperatures(self, tempratures: list[int]):
		result =[0]*len(tempratures)
		stack = []

		for i , t in enumerate(tempratures):
			while(not not stack and t > stack[-1][0]):
				result[stack[-1][1]] = i - stack[-1][1]
				stack.pop()

			stack.append([t ,i])


		return result













