class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [None] * 2 * length
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + length] = nums[i]
        return ans