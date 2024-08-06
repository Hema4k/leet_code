class Solution:
	def checkInclusion(slef, s1: str, s2: str):
		l = 0
		r = len(s1)
		target = sorted(s1)
		while(r<len(s2)+1):
			window = s2[l:r]
			if(sorted(window) == target):
				return True
			l+=1
			r+=1
		return False

x = Solution()
print(x.checkInclusion("hello", "abgooolleeeeolleh"))