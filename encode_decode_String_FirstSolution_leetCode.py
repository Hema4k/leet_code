class Solution:
	def encode(self, lis :list) -> str:
		result = ""
		for s in lis:
			result = result + str(len(s))+"#"+s
		return result


	def decode (self, s: str) -> list:
		result = []
		i = 0
		while i < len(s):
			if(s[i]== "#"):
				length= int(s[i-1])
				result.append(s[i+1:i+1+length])
				i = i + length
			i+=1
			
		return result




