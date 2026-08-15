class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1   

        buckets = [[] for _ in range(len(nums)+1)]
        for num,freq in dict.items():
            buckets[freq].append(num)
        result = []

        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result                   