class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = float('inf')
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                # search the left side, so r = mid
                r = mid
            else:
                # search the right side, so l = min + 1
                l = mid + 1
        if l == r:
            min = nums[l]
        return min
        