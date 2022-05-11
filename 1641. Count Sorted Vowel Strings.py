class Solution:
"""
Runtime: 34 ms, faster than 77.85% of Python3 online submissions for Count Sorted Vowel Strings.
Memory Usage: 13.9 MB, less than 27.46% of Python3 online submissions for Count Sorted Vowel Strings.
"""
    def countVowelStrings(self, n: int) -> int:
        #return math.comb(n + 4, n)
        
        #u = [1]*n
        #o = range(1,n+1)
        i = [1]
        for index in range(1,n):
            #print(o[index])
            i.append(i[index-1]+index+1)
        #print('i:',i)
        e = [1]
        for index in range(1,n):
            e.append(e[index-1]+i[index])
        #print("e:",e)
        
        #a = [1]
        #for index in range(1,n):
        #    a.append(a[index-1]+e[index])
        #print("a:",a)
        
        a = sum(e) # only need the last one for calculation
        return 1+n+i[n-1]+e[n-1]+a
