from collections import deque
class Solution:
	def validParenthese(self, s: str) -> bool:

		parenthese = {"]":'[', "}": "{", ")":"("}
		stack = []
		if len(s)%2 != 0:
			return False

		for char in s:
			if char not in parenthese:
				stack.append(char)
				#append every open parenthese

			else:
				if(not stack):#if there is closing parenthese
								#and stack empty return False
					return False

				else: 
					top = stack.pop()
					if(top != parenthese[char]):
						return False
						# check if the last open parenthese in the stack
						# matches the new new closing parenthese from the string
						#using the hash map

		return not stack 
		# if the stack is not empy there are opened parenthse with no closing


	







x = Solution()
print(x.validParenthese("{{"))
