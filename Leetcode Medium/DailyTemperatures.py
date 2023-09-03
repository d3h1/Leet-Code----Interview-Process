class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # PROBLEM UNDERSTANDING
        # Output has to be the amount of days ahead of a certain index in temperatures where the next temperature is greater than the current one

        answer = [0] * len(temperatures)
        stack = [] # Will take out temps and append or pop based on values

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # check the stack and see if cur temp is greater than previous
                stackT, stackInd = stack.pop() # if it is greater - we want to pop the previous index and stack
                answer[stackInd] = i - stackInd # to get the length between them, we want to take the current "greater values index" and then subtract the "less than values index from it". THIS IS HOW WE GET NUMBER OF DAYS BETWEEN
            stack.append((t,i)) # we only that previous step if those conditions are good. once done, we would append the temp pair that ended up with that current for loop iteration. 
        return answer # once the for loop is done, we know that the answer that is appended to finally is good to go