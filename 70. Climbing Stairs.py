from math import factorial
class Solution:
    def climbStairs(self, n: int) -> int:
        # Newton's method 
        #https://www.youtube.com/watch?v=Y0lT9Fck7qI
        
        x = x_1 = 1
        for _ in range(n):
            #print(x,x_1)
            x ,x_1 = x_1, x + x_1
            
        return x
        """
        if n == 0:
            return 0
        
        step = 1 
        one = n
        two = 0
        
        while one - 2 >= 0:
                one -=2
                two +=1
                
                step += factorial(one+two)/(factorial(one)*factorial(two))
                
                #print("one:",one," two:",two,"step: ",step)
        return int(step)
        """
        
       
        
        
            
        
        
