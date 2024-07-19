class Solution:
	def topKFrequent(self, nums: list, k: int):
		map ={}
		sol = []

		for i, num in enumerate(nums):
			if num in map:
				map[num] = map[num] +1
			else:
				map[num] = 1

		for j in range(k):
			maxValue = max(map.values())
			key = [str(m) for m, v in map.items() if v == maxValue]
			newKey = int(str(''.join(key[-1])))
			map.pop(newKey)
			sol.append(newKey)
	
		return sol

		
# Explanation
# First, using a loop I put every unique elements in a hash map as a Key
# then I count how many times the element shows up and put the count
# in the value corresponding to the key(element) in the hash map.

# For the second for loop, I see which value is the highest form the values list and bring back 
# its key, or  group of keys.
# I take only one key from the list the list of keys, and turn the chosen key from a list to a an int
# lastly I append the found key in (sol) list, and pop the key from the map, so if the loop iterate anymore
# the max() won't bring the same key again since it was deleted from the hash map
# time take: <1 hr  
