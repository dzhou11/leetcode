class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
Runtime: 138 ms, faster than 77.43% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 14.8 MB, less than 54.32% of Python3 online submissions for Set Matrix Zeroes.
"""
        rows = []
        cols = []
        for i,row in enumerate(matrix): # find rows and columns
            if 0 in row:
                rows.append(i)
                cols.extend([i for i in range(len(row)) if row[i]==0])
                
        zeros = [0]*len(matrix[0]) # a zero row
        
        for i in range(len(matrix)): # update to 0
            if i in rows:
                matrix[i] = zeros
            else:
                for c in set(cols):
                    matrix[i][c] = 0
        
