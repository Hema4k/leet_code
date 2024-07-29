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
# the stack will contenousely store values in descending order
# plus the index of the value in temperatures list in [ vlaue, index] format
# with the top of the stack being the smallest value, so each value form
# temperatures list will be compared to the top of the stack only, and pop 
# if and the (new top of the stack) if it is smaller than the value
# from temperatures list, th we also compare to it 
# in case the new value is bigger than the top of the stack
# we substract the index of the new value in temperatures from the index
# of the value which is stored in the stack 
# meaning ( i - stack [-1, 1]  )
# I put it in a while instead of if to continuosly chich if the new stack top
# after the pop is still smaller the the currenct Temperatures[i]












