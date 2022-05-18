class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # write your code here

        # edge case
        if k==0:
            return 0

        charlist  =  []
        out = 0
        curr = 0
        l = 0

        for r in range(len(s)):

            if s[r] in charlist: # seen before 
                curr += 1
                charlist.append(s[r])
                
            else: # new element
                
                if len(set(charlist)) < k: # able to add 
                    curr+=1
                    charlist.append(s[r])
                else: # not able to add
                    
                    while len(set( charlist ))>=k: # remove the left most element until the size get lower than k 
                        charlist.pop(0)
                        
                        curr -=1 
                    curr+=1
                    charlist.append(s[r])
            
            out = max(curr,out)
        return out

                    



