class MinStack:
    # Create the constructor for MinStack
    def __init__(self):
        # We create empty stacks for both (a regular stack and a min stack that stacks value to)
        self.stack = []
        self.minStack = []
        
    # Create the push functionality
    def push(self, val: int) -> None:
           # First stack is easily appendable
           self.stack.append(val)
           # Min stack needs a checker as val being appended can be cur val or top of stack if stack is non-empty
           val = min(val, self.minStack[-1] if self.stack else val)
           self.minStack.append(val)

    # Create the pop functionality
    def pop(self) -> None:
        # Popping is pretty straight forward -- just use pythons built in pop functionaility
        self.stack.pop()
        self.minStack.pop()
    
    # Create the top functionality
    def top(self) -> int:
        # Only need to return stack with top as we will use getMin for the minStack
        return self.stack[-1]

    # Create the get min functionality
    def getMin(self) -> int:
        # Use get min for the top of the minStack
        return self.minStack[-1]
    
# TIME COMPLEXITY : O(1) -- Constant time needed for each function here
