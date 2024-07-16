class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
      
        s1 = ''.join(sorted(s.lower()))
        t1 = "".join(sorted(t.lower()))
        
        if s1 == t1:
            return True
        else:
            return False

        
    
x = Solution()
print(x.isAnagram("ehollGh", "hollehg"))