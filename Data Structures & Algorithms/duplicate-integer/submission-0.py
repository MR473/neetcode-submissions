class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = []
        for i in range(len(nums)):
            if nums[i] in exists:
                return True
            else:
                exists.append(nums[i])
        return False


    
