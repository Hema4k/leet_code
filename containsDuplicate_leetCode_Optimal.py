class Solution(object):
    def containsDuplicate(self, nums):
        seen = dict()
        for i in range(len(nums)):
            if(len(nums)<1 and len(nums)>10**5 or nums[i]<-10**9 or nums[i]>10**9):
                return "sorry invalid input"
            if(nums[i] not in seen.keys()):
                seen.update({nums[i]:0})
                
            else:
                return True        

        return False

#addin this is the most optimal solution using a hash table/map 

 


