class Solution():
	def threeSum(self, nums: list[int]):
		result = []
		nums.sort()




		for i, num1 in enumerate(nums):
			if i > 0 and num1 == nums[i-1]:
				continue

			left = i + 1
			right = len(nums)-1
			while(left<right):
				sum = num1 + nums[left] + nums[right]

				if(sum<0):
					left+=1

				elif(sum >0):
					right-=1

				else:
					result.append([num1, nums[left], nums[right]])
					left+=1
					while (nums[left]== nums[left-1] and left<right):
						left+=1
					
		return result
		




# the way to solve this is similar to two Sum II, the difference is you sort
# the list yourself, and makes a for loop to give one of the 3 numbers a value
# from the list starting from nums[0], and then solve the problem with two pointers
# like two Sum II, and note in the end we make a while loop, to prevent duplicate, since
# array is sorted, the duplicates wil be right next to each other, that means the number and
# and it's duplicate are always next to each other, and of course make sure i < j doing that 

