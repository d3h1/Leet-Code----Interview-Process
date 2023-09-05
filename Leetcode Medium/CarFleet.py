# Can be solved in linear time. Each point is a point on a graph with the slope of their speed. This is how we can determine which one gets to the target first

# Can be done right to left --- reverse order allows for things to not collide into each other

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)] # List comrehension

        stack = [] # Carfleets at end

        for p, s in sorted(pair)[::-1]: # Reverse Sort
            stack.append((target - p) / s) # !THIS IS THE TIME --  decimal division as we dont want integer division
            # *If it has atleast two cars and if time that top of stack reaches before the one ahead of it --- this must mean THEY COLLIDE causing a car fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:  
                stack.pop() # !decreasing amount of carfleets -- combining cars to one basically
        
        return len(stack)
    
    #! TIME COMPLEXITY : O(nlogn) -- due to sorting
    #! SPACE COMPLEXITY : O(n)