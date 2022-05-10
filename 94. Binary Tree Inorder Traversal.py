# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
Runtime: 34 ms, faster than 75.21% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14 MB, less than 13.52% of Python3 online submissions for Binary Tree Inorder Traversal.
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #return self.reg(root,[])   
        return self.reg(root)
    """ my original solution
    def reg(self, node, path):
        if node == None:
            return path
        if node.left != None:
            return path  + self.reg(node.left, []) + [node.val] + self.reg(node.right,[])
        elif node.right != None:
            return path  + [node.val] + self.reg(node.right,[])
        else: 
            return path  + [node.val]
    """
    def reg(self,node): # a simpler one
        if node == None:
            return []
        return  self.reg(node.left)+[node.val] + self.reg(node.right)
        
        
