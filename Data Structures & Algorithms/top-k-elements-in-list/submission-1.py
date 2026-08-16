class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        temp = []
        
        while len(temp) != k:
            key = max(dict,key = dict.get)
            temp.append(key)
            del dict[key]
        return temp

                       

                     