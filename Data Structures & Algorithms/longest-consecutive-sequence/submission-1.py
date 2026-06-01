class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current_length = 1
                current_num = num
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1
                if current_length > longest:
                    longest = current_length
        return longest
