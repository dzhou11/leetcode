class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        # Runtime: 56 ms, faster than 28.44% of Python3 online submissions for Subsets.
        # Memory Usage: 14.2 MB, less than 33.95% of Python3 online submissions for Subsets.
        
        out = [[]]
        for i in nums:
            out.extend([l+[i] for l in out])
        return out
        """
        
        def backtrack(start=0, path =[]):
            if len(path) == k:
                out.append(path[:])
                return 
            
            for i in range(start, n): 
                path.append(nums[i])
                backtrack(i+1, path )       
                path.pop()
                    
        out = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return out
        
        
    
