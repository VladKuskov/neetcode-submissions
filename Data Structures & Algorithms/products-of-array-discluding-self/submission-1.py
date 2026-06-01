class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        for i in range(len(nums)):
            temp = 1
            # for all other elements other than the element at index i, multiply then by temp, and
            # store the product
            for j in range(len(nums)):
                if j != i:
                    temp *= nums[j]
            product.append(temp)
        return product