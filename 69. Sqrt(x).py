class Solution:
    def mySqrt(self, x: int) -> int:
        """ cheating method
        return int(sqrt(x))
        """
        
        """ my search method
        out = x 
        while True:
            #print(out)
            if out**2 <= x:
                if (out+1)**2 > x:
                    return out
                else:
                    out = (out+out//2)
            else:
                out = (out-out//2)
        """
        
        """ Newton Method https://www.youtube.com/watch?v=cf_NK7NlWrs
        r = x
        while r**2 > x:
            r =  ( r + x / r )//2
        return int(r)
        """
