class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        # the final subarray has to end at some element
        # find the largest sum end at each element
        curr = out = nums[0]
        
        for i in nums[1:]:
            if curr > 0:
                curr += i 
            else:
                curr = i
            out = max(out,curr)
                
        return out
        
