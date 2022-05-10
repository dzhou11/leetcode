class Solution:
    """
Runtime: 31 ms, faster than 91.43% of Python3 online submissions for Combination Sum III.
Memory Usage: 13.9 MB, less than 29.59% of Python3 online submissions for Combination Sum III.
    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k>n or n > 45: # extreme case
            return []
        return self.helper(k,n,[])
            
    def helper(self,k, n, comb):
        if len(comb)==k: # a path with correct length
            if sum(comb)==n:
                return [comb] # correct path
            else:
                return [] # incorrect
        
        out = []
        # use this aRange to deal with initial case
        aRange = range(comb[-1]+1,min(n,10)) if comb !=[] else range(1,min(n,10))
        for i in aRange:
            if sum(comb)+i>=n and len(comb)+1<k: 
            # already sum to n, the cases after this point is not worth condisering
                break
            out.extend(self.helper(k,n,comb+[i]))
        return out
            
        
            
        
