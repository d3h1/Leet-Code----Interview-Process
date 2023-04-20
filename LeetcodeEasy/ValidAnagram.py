class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Before answering the question, we should determine if the strings are the same length
        if len(s) != len(t):
            return False
        
        # Then we will declare empty hashmaps as lookup tables
        countS, countT = {}, {}
        
        # We use the length of S as we know that matches the length of T also
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countS[s[i]] = 1 + countS.get(s[i], 0)
        return countS == countT
        