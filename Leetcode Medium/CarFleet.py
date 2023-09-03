class Solution:
    def CarFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        stack = []
        
        for p,s in pair:
            stack.append((target - p) / s) # we do this to get the value from target based on position and speed
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # we pop values that are greater than a length of 2 as well as less than the value before it
        return len(stack)