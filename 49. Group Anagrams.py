class Solution:
    """
Runtime: 102 ms, faster than 88.59% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.6 MB, less than 72.90% of Python3 online submissions for Group Anagrams.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {} # a hashmap
        for string in strs:
            key = str(sorted(list(string))) # make a hash key
            if key in dic:
                dic[key].append(string)
            else:
                dic[key] = [string]
        return list(dic.values())
