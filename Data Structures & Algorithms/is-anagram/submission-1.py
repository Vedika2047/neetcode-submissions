class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        count = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1                 
        for i in t:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1 
        if freq == count:
            return True
        else:
            return False                            
        