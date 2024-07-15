class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            if(len(nums)<1 and len(nums)>10**5 or nums[i]<-10**9 or nums[i]>10**9):
                return "sorry invalid input"
            
            for j in range(len(nums)):
                if(i!=j and nums[i]== nums[j]):
                    return True
        return False

