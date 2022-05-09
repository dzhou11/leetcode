class Solution:
    """
Runtime: 39 ms, faster than 92.58% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 59.62% of Python3 online submissions for Permutations.
    """
    # helper method to carry out regression duty
    def reg(self,out, rest):
        if len(rest) ==1: # base case, only one element to append
            return [out+rest]
        # regressive step: a
        outs = []
        for i in rest:
            outs.extend(self.reg(out+[i],[j for j in rest if j!=i]))
        return outs
    
    # main function 
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.reg([],nums)
    
    
        
        
