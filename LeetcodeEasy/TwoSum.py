class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have to define an empty hash table to be our look up table
        prevValues = {}
        
        # for loop to get the most efficient time
        for i,n in enumerate(nums): # *[(0,2),(1,7),(2,11),(3,15)] Enumerate can give us ths based on the array provided
            diff = nums[i] - target
            if diff in prevValues:
                return [prevValues[diff], i]
            # *if this is not true, we look to the next index and add this previous one to the look up table
            prevValues[n] = i
        return