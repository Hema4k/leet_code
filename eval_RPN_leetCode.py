class Solution:
	def evalRPN(self, tokens: list[str]) -> int:

		operations = {"+":"+", "-":"-", "/":"/" ,"*":"*"}
		nums = []

		for s in tokens:  
			if s not in operations:
				nums.append(int(s))

				
			else:

				if(operations[s] == "+"):
					if(not not nums):
						num1  = int(nums.pop())
						if (not not nums ):
							num2 = int(nums.pop())

						nums.append(num2+num1)


				if(operations[s] == "-"):
					if(not not nums):
						num1  = int(nums.pop())
						if (not not nums ):
							num2 = int(nums.pop())

						nums.append(num2-num1)



				if(operations[s] == "*"):
					if(not not nums):
						num1  = int(nums.pop())
						if (not not nums ):
							num2 = int(nums.pop())



						nums.append(num2*num1)

				if(operations[s] == "/"):

					if(not not nums):
						num1  = int(nums.pop())
						if (not not nums ):
							num2 = int(nums.pop())
						nums.append(int(num2/num1))
						

		return int(nums[0])
										