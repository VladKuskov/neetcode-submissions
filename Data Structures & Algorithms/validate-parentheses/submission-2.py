class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')': '(', ']': '[', '}': '{'}
        stack = []

        if len(s) == 1:
            return False

        # for each char in s:
        # if char is open bracket, push to stack
        for c in s:
            if c in "([{":
                stack.append(c)

            # if char is a key in matches, means it's a closed bracket
            if c in matches:
                # if the stack not empty, and the last value in stack equals
                # matches[c], then pop it off.

                #ex: c = '}', stack = ['(' ,'[' ,'{' ]
                # matches[c] = '{', so pop:
                # stack = ['(' ,'[']
                # now c is ']' so repeat.
                if stack and stack[-1] == matches[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0        