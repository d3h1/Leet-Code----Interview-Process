class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # We need to use a hash set -- Cancels the possibility of a duplicate which allows for more efficient lookup. We are able to return True as soon as it notices a duplicate.
        
        emptyHash = set() # Declare our hash set
        
        for n in nums: # Loop through the integer array
            if n in emptyHash: # Check if number is already present in hash set
                return True # Return true if number is already present
            emptyHash.add(n) # Add number to hash set if not present
        return False # Once loop is complete, if no duplicates found, then return False
    