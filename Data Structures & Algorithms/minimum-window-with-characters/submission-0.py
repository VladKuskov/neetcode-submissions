class Solution:
    def minWindow(self, s: str, t: str) -> str:
            # 1. Count what letters we need
        needed_letters = Counter(t)
        missing_total = len(t)

        # 2. Setup our boundaries and the best answer we found
        left = 0
        best_start = 0
        shortest_length = float("inf")

        # 3. Stretch the right side out
        for right in range(len(s)):
            right_char = s[right]

            # If this letter is one we need, count it towards our goal
            if needed_letters[right_char] > 0:
                missing_total -= 1

            # We take the letter into our window
            needed_letters[right_char] -= 1

            # 4. If we have ALL the letters, try to shrink from the left
            while missing_total == 0:
                # Check if this is the smallest window we have ever seen
                current_length = right - left + 1
                if current_length < shortest_length:
                    shortest_length = current_length
                    best_start = left

                # Now, kick out the leftmost letter and move left forward
                left_char = s[left]
                needed_letters[left_char] += 1

                # If kicking it out means we don't have enough of that letter anymore...
                if needed_letters[left_char] > 0:
                    missing_total += 1  # We are missing a letter again!

                left += 1

        # If shortest_length never changed, we found nothing
        if shortest_length == float("inf"):
            return ""

        # Return the best slice we found
        return s[best_start : best_start + shortest_length]