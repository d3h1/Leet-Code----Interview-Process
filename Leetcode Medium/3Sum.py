class Soltution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We want to initially sort the array
        nums.sort()
        
        # We then will create a results array that will hold our triplet arrays
        res = []
        
        # We will initiate a for loop using enumerate to get the index and value at that index
        for i, n in enumerate(nums):
            
            # Checking if it is a value after the first and checking if the value at that index is the same before it. Basically allowing us to skip that value to get rid of duplicate values
            if i > 0 and n == nums[i - 1]:
                continue
                
            # We will then initiate our pointers. The pointer will come after the value we are looking at. 
            l, r = i + 1, nums[i - 1]
            
            # Initiate a two pointer methodology for the pointers after "n"
            while l < r:
                # Three sum is the value of all three values to see if they equal zero.
                threeSum = n + nums[l] + nums[r]
                
                # Do If Else to if we have to move a pointer and which one
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # We do this for the left pointer only so we dont get duplicates on that left pointer. We dont need to for the right because it is constantly moving from the end
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
    
                    
        return res
                    
            