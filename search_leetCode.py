class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lower = 0
        upper = len(nums)-1
        i = 0
        
        while i < len(nums):
            curln = (lower + upper)//2 
            if(nums[curln] == target):
                return curln       
            if(nums[curln] < target):
                lower = curln+1
            else:
                upper = curln-1

            if(lower> upper):
                return-1

            i+=1





x = Solution()
print(x.search([-1,0,3,5,9,12],-1))