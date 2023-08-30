class MinStack:
    # Create the constructor for MinStack
    def __init__(self):
        # We create empty stacks for both (a regular stack and a min stack that stacks value to)
        self.stack = []
        self.minStack = []