from collections import defaultdict
class Solution:
	def groupAnagrams(self, input: list ):
		anagrams = defaultdict(list)
		
		for string in input:
			count = [0]*26

			for char in string:
				count[ord(char) - ord('a')] +=1

			key = tuple(count)

			anagrams[key].append(string)
		return anagrams.values()


