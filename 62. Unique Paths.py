from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #numinator: treat every down as unique, every right as unique
        #demoninaator: for a same up&down combination, how many duplicate counts happended(duplicate caused by thinking each down movement is unique)
        return int(factorial(n+m-2)/ (factorial(n-1)*factorial(m-1)))
