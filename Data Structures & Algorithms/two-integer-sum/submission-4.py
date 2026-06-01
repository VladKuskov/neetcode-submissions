class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            difference = target - nums[i]
            if difference in seen:
                return [seen[difference], i]
            seen[num] = i
        
        return output
                



            




