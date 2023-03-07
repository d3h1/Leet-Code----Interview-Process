class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # This method will sort the two strings by letter in order and help create a time complexity of O(1) by comparing the two orders
        return sorted(s) == sorted(t)
        
        
        # Check if length of strings is the same before anything 
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            # So we are looking at the letter through countS[s[i]] and adding 1 each time it is found in the string
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # We do this for loop to check the count of each
        for c in countS:
            if countS[c] != countT.get(c):
                return False
        
        return True