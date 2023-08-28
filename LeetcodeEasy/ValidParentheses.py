class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Declare an empty stack 
        map = {")" : "(" , "}" : "{", "]" : "["} # Mapping out the closing brackets to their respective opening brackets to make it easier to identify
        
        # Looping through each character in s
        for c in s:
            
            if c not in map: # If c is not in map, this means it is not a closing bracket so we simply append it to the top of the stack
                 stack.append(c)
                 continue # We hit continue after the append to go the next character and not do the next part of the loop
            if not stack or stack[-1] != map[c]: # If stack is empty or the top of the stack does not equal a value of c in the map, we return false
                return False
            stack.pop() # WE pop everytime we fnd a pair
            
        return not stack # Return true or false based on if the stack is empty or not