class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Using a set to get all the unique elements from the nums array
        numSet = set(nums)
        longest = 0
        
        # We have to run through each number in the nums list 
        for n in nums:
            # This is checking the left of that number
            if n - 1 not in numSet:
                length = 1
                # SO if there is no left, we start with that one to make a sequence and continue forwards until we do not have a consecutive length 
                while (n + length) in numSet:
                    length += 1
                # Getting the longest from the length
                longest = max(length, longest)
        return longest
