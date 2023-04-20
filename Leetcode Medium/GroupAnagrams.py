import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # So we are given an array of strings, and we have to check the ltters of each string to group strings that are anagrams of each other.
        # We can do this in a o(m*nlogn) time complexity using sorting methods, but it would be better to use Hashmaps to achieve a faster time complexity og o(m*n*1)
        
        # TO DO THIS -- we can declare a hashmap as a defaultdict to not raise key errors if a character is not found in the string we are looking at
        # WE will also use count to keep count of the number letters we get per string
        
        res = collections.defaultdict(list) # defining list as a parameter
        
        # WE can use the array as our first loop or rather the 'm'
        for s in strs:
            count = [0] * 26 # declaring 0 to give the letters a place to go in terms of counting, we also declare them through their indexes using ascii chars a.....z
            for c in s: #the s is the string it self and that will be our 'n'
                count[ord(c) - ord('a')] += 1 # we are using the chars ascii values to get their index and add 1 to their count
            res[tuple(count)].add(s) # we are using the count of characters to be arranges into similar groups based on their strings
        return res.values()
            