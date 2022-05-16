class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        dutch partitioning problem
        one pass solution
        """
        zero = 0
        one = 0 
        two  = len(nums)-1
        while one <= two:
            if nums[one] == 0:
                nums[one], nums[zero] = nums[zero], nums[one]
                
                zero += 1
                one += 1
            elif nums[one] ==1:
                one +=1
            else:
                nums[two], nums[one]  = nums[one], nums[two]
                two-=1
        """
        zero = 0 
        one = 0
        for i in range(len(nums)):
            
            if nums[i] == 0:
                
                nums[zero] = 0
                zero += 1
            
            elif nums[i] == 1:
                one +=1
            
        nums[zero:zero+one] = [1]*one
        nums[zero+one:] = [2]*(len(nums)-one-zero)
        """
        
