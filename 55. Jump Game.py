class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        m = 0 # the farest it can reach for now
        for i in range(len(nums)):
            if i > m: # if we definately cannot go beyound a certain point
                return False
            m = max(m,i+nums[i])
        return True
            
            
    
        
