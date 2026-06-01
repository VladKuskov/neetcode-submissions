class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums = [3, 4, 5, 6, 1, 2]
        # target = 1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # if 5 >= 3 mid belongs to the left portion
            if nums[mid] >= nums[l]:
                #if the target is larger than nums[l] and smaller than nums[mid], it belongs in that half.
                # move right pointer to search the left side.
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                # target < nums[l], so search the right slide.
                else:
                    l = mid +1
            # else, mid belongs to the right portion
            else:
                if target >= nums[mid] and target <= nums[r]:
                    #target in right portion
                    l = mid + 1
                else:
                    # target in the left portion
                    r = mid - 1
        return -1