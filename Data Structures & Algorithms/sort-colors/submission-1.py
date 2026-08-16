class Solution:
    def sortColors(self, nums: List[int]) -> None:
        col0 = 0
        col1 = 0
        col2 = 0
        for i in nums:
            if i == 0:
                col0 += 1
            elif i == 1:
                col1 += 1
            else:
                col2 += 1
        for i in range(len(nums)):
            if col0 > 0:
                nums[i] = 0
                col0 -= 1
            elif col1 > 0:
                nums[i] = 1
                col1 -= 1
            else:
                nums[i] = 2
                col2 -= 1        
        return nums                            