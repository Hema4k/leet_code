class Solution():
	def dailyTempratures(self, tempratures: list[int]):
		result =[0]*len(tempratures)
		stack = []

		for i , t in enumerate(tempratures):
			while(not not stack and t > stack[-1][0]):
				result[stack[-1][1]] = i - stack[-1][1]
				stack.pop()

			stack.append([t ,i])


		print(result)












x =Solution()
print(x.dailyTempratures([30,38,30,36,35,40,28]))
