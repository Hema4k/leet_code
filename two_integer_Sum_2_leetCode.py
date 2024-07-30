class Solution():
	def twoSum(self, nums: list[int], target: int):
		i = 0
		j = len(nums) -1
		mapI = {}
		mapJ = {}
		while(i-1<=j):


			diffI = target- nums[i]
			diffJ = target- nums[j]

			if(nums[i] in mapI):
				return [ mapI[nums[i]]+1,i+1]

			if(nums[j] in mapI):
				return [ mapI[nums[j]]+1,j+1,]

			if(diffI in mapJ):
				return [i+1,mapJ[diffI]+1]

			if(diffJ in mapJ):
				return [j+1,mapJ[diffJ]+1]


			mapI[diffI] = i
			mapJ[nums[j]] = j

			i+=1
			j-=1
		return []


# this is another original solution
# I used two pointers approach to navigate the list of integers
# from left to right usin index i, and from right to left using index j
# it's close to two sum first problem, but we use in both ways using two
# hash maps.

# mapI stores in each key the number we need to add to the numeber in the index (value)
# to get  the target, simply ( key + nums[value] = target)
# we do the same thing from right to left with J index
# but we store the elements as they are in mapJ, not difference like mapI

# what we are doing is to see if the nums[i] we currently see is in mapI, meaning if we have seen 
# it's compliment/difference a number we add nums[i] to to give us target
# we also see if nums[j] coming from the left is in the mapI 

# we also check if diffJ(target - nums[j]) is in mapJ, meaning if the there is compliment numberin mapJ to nums[j]
# that will give us target
# we do the same thing with diffI(target-nums[i]), to see if there is number in mapJ we add to nums[i] to get target




