class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        result = False
        for i in nums:
            if i in temp:
                result = True
                break
            else:
                temp.append(i)
        return result            
           
           
        
