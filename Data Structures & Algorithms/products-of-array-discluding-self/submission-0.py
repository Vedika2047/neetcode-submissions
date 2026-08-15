class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        sufix = [1]*len(nums)
        #prefix
        product = 1
        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i] 
        # suffix
        product = 1
        for i in range(len(nums)-1,-1,-1):
            sufix[i] = product
            product *= nums[i]  
        #product of array
        for i in range(len(nums)):
            nums[i] = prefix[i] * sufix[i]

        return nums          
