class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using count hashmap to count occurences of the values
        count = {}
        # Special array that will be same size as input array, index is frequencyof elelent and count will be list of values at that index(number of times)
        freq = [[] for i in range(len(nums) + 1)] # number of empty arrays that go in the size of our input
        
        # Counting the amount of times each value in nums occurs
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        for n, c in count.items():
            freq[c].append(n) # Count is gonna be the index, this value occurs exactly c times

        
        res = [] # Top K Elements
        # Descending order because we want to start with numbers that occur the most
        for i in range(len(freq) - 1, 0, -1): # lastIndex, goToBeginning, reverseOrder
            # Go through every value in frequency at index i because every item inserted to i is another sublist (empty, or values)
            for n in freq[i]:
                res.append(n) # Getting the n value that occurs most frequently
                if len(res) == k:
                    return res

        
        #! WITH HEAPIFY it would be O(klogn) so we used a hashmap to get this to O(n)! #