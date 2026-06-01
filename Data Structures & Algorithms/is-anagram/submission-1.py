class Solution:

    s = "pracecar"
    t = "carrace"

    # compare len() of s & t, and char counts in the strings
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        #since theyre the same len(), just iterate over s
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for key in countS:
            #.get(), because what if countS has a key that countT doesn't have?
            if countS[key] != countT.get(key, 0):
                return False

        return True

        
                
