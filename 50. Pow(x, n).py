class Solution:
    """
Runtime: 29 ms, faster than 90.14% of Python3 online submissions for Pow(x, n).
Memory Usage: 13.9 MB, less than 69.47% of Python3 online submissions for Pow(x, n).
    """
    def myPow(self, x: float, n: int) -> float:
        # turn negative n to positive n 
        if n < 0:
            x= 1/x
            n = -n
        #base case
        if n == 0:
            return 1 
        elif n == 1:
            return x
        # regression step
        elif n%2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return x * self.myPow(x*x, n//2)
        
