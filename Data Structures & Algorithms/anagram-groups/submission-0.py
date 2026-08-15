class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            freq = [0] * 26

            for ch in s:
                freq[ord(ch)-ord('a')] += 1 #ord ae character ni ASCII values ape che (a mate 97)
            key = tuple(freq)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)    

        return list(groups.values())