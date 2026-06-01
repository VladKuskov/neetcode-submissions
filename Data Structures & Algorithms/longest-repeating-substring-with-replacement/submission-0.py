class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        max_len = 0
        for r in range(len(s)):

            if s[r] in counter:
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1
            window_size = r - l + 1
            if window_size - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
                window_size = r - l + 1
            
            if window_size > max_len:
                max_len = window_size
        return max_len