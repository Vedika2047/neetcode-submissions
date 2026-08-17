class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict = {}
        n = len(nums)
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        temp = []
        for key in dict:
            if dict[key] > n//3:
                temp.append(key)
        return temp                    
        