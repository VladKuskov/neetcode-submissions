class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            # add new num as a key in dict if its not there. iterate its 0 to 1.
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        sorted_keys = sorted(counts, key=lambda x: counts[x])
        print(sorted_keys[-k:])
        return sorted_keys[-k:]