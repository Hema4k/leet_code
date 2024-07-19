class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        
        if len(nums)>10**4 or len(nums)<2:
            return[]
        if target >10**9 or target<-10**9:
            return[]

        map = {}

        for i, num in enumerate(nums):
            if(nums[i]> 10**9 or nums[i]< -10**9):
                return []
            complement = target - num

            if complement in map:
                return [map[complement], i]
            map[num] = i
                
        return[]
 
#final solution using hash map