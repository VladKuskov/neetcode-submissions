class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = dict()
        window_count = dict()
        result = ""
        # t_count dict
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        have, need = 0, len(t_count)
        l = 0
        for r in range(len(s)):
            # start iterating through s
            if s[r] not in window_count:
                window_count[s[r]] = 1
            else:
                window_count[s[r]] += 1

            if s[r] in t_count and window_count[s[r]] == t_count[s[r]]:
                have += 1

            while have == need:
                if result == "" or (r - l + 1) < len(result):
                    result = s[l:r+1]
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        return result