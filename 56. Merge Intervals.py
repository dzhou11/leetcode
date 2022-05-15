class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
Runtime: 165 ms, faster than 68.59% of Python3 online submissions for Merge Intervals.
Memory Usage: 18.2 MB, less than 52.35% of Python3 online submissions for Merge Intervals.
        """
        intervals.sort()
        out = [intervals[0]] 
        
        for i in range(1,len(intervals)):
            if out and out[-1][1] >= intervals[i][0]:
                out[-1]=([out[-1][0],max(intervals[i][1],out[-1][1])]) # merge two
            else:
                out.append(intervals[i]) # cannot merge, add to list
                
        return out
