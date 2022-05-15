class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
"""
Runtime: 36 ms, faster than 79.68% of Python3 online submissions for Plus One.
Memory Usage: 13.8 MB, less than 96.92% of Python3 online submissions for Plus One.
"""          
        r = digits[-1]+1 
        carry = r//10
        digits[-1] = r%10
        
        for i in reversed(range(len(digits)-1)):
            
            r =  digits[i]+carry
            carry = r//10
            digits[i] = r%10
        if carry == 1:
            digits=[1]+digits
        return digits
