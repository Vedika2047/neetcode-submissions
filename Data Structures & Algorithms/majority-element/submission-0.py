class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1

        max_c = 0
        val = 0         
        for key in dict:
            if dict[key] > max_c:
                max_c = dict[key]
                val = key
        return val                
        