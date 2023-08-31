class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # We init our empty stack to hold each number of the list
        
        # for loop to get to every character in the list
        for c in tokens:
            # we will do a condition for every operator that comes up
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a)) # Floating point division allows us to round to the nearest 0
            else:
                stack.append(int(c))
        return stack[-1] # Always valid because there will always be the last value in the stack which is the last outpt