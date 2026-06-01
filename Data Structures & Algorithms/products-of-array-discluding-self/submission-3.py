class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        # calculating the prefix
        p = 1
        for i in range(len(nums)):
            prefix.append(p)
            p *= nums[i]
        #calculating the suffix
        s = 1
        # start at len(nums)-1, stop at i = -1, and increment by -1:
        for i in range(len(nums) - 1, -1, -1):
            suffix.insert(0, s)
            s *= nums[i]

        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result