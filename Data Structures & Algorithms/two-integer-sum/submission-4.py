class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = list()
        for i in range(len(nums)):
            val = target - nums[i]
            if val in l:
                return [l.index(val), i]
            else:
                l.append(nums[i])
        