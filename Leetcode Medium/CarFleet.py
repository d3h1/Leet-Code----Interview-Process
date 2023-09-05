# Can be solved in linear time. Each point is a point on a graph with the slope of their speed. This is how we can determine which one gets to the target first

# Can be done right to left --- reverse order allows for things to not collide into each other

class Solution:
    def CarFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse=True) # This is the reasoning behind reversing it. The values that are at bottom will be on top so we can add to the stack right to left
        
        stack = []
        
        for p,s in pair:
            stack.append((target - p) / s) # we do this to get the value from target based on position and speed
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # we pop values that are greater than a length of 2 as well as less than the value before it
        return len(stack)
    
    #! TIME COMPLEXITY : O(nlogn) -- due to sorting
    #! SPACE COMPLEXITY : O(n)