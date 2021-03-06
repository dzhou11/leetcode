class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
Runtime: 30 ms, faster than 88.84% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.9 MB, less than 33.71% of Python3 online submissions for Spiral Matrix.
        """
        #print( [*zip(*matrix)] )
        #print( [*zip(*matrix)][::-1])
        #return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        # [*zip(*matrix)][::-1]
        
        top = 0
        bottom = 0
        left = 0
        right = 0
        
        out = []
        
        x = len(matrix[0])-1
        y = len(matrix)-1
        length = len(matrix[0])*len(matrix)
        
        while len(out)<length:
            #print(out,top,bottom,left,right)
            
            if top == bottom and left == right: # add top
                out.extend(matrix[top][left:x - right+1])
                top+=1
                
            elif top >bottom and left == right: # add right
                for i in range(top, y-bottom+1):
                    #print(matrix[i][x-right])
                    out.append(matrix[i][x-right])
                right += 1
            elif top>bottom and left<right: # add bottom
                temp = list(reversed(matrix[y-bottom][left:x - right+1]))
                out.extend(temp)
                bottom+=1
            else: # add left
                for i in range(top, y-bottom+1):
                    out.append(matrix[y-i][left])
                left += 1
        return out
