class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()
        for x in nums:
            if x in unique_set:
                return True
            unique_set.add(x)
        return False
        