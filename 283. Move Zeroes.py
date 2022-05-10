class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
Runtime: 179 ms, faster than 79.46% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.5 MB, less than 97.43% of Python3 online submissions for Move Zeroes.
        """
        if len(nums)==1: # edge case
            return 
        cnt = 0
        
        for i in range(len(nums)):
            if nums[i]==0: # count 0
                cnt+=1
                
            else: # if this number isn't 0
                nums[i-cnt] = nums[i]  # copy this number "cnt" index before 
                if cnt >0: 
                    nums[i] = 0 # if there is any 0 before, this place should be 0
            
            
        
        
