from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # mid = k
        # if eat mid bananas/hr, can you finish in time h?
        l, r = 1, max(piles)
        mid = 0
        result = max(piles)
        while l <= r:
            mid = (l + r) // 2
            if sum(ceil(pile/mid) for pile in piles) <= h:
                # if true, try a slower mid/k
                result = mid
                r = mid - 1
            else:
                # false, so try a faster mid/k, increment l
                l = mid + 1
        return result