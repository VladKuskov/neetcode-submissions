class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ex: nums = [-1,0,2,4,6,8] target = 4
        l, r = 0, len(nums) - 1
        mid = 0

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
