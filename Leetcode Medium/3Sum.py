class Soltution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We want to initially sort the array
        nums.sort()
        
        # We then will create a results array that will hold our triplet arrays
        res = []
        
        # We will initiate a for loop using enumerate to get the index and value at that index
        for i, n in enumerate(arr):
            