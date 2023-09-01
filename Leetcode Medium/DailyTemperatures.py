class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List:
        # We want to declare the answer array like the problem says here
        # Use the length of the temperatures to keep consistent length outputs to each number in that OG list
        answer = [0] * len(temperatures)
        
        # We then declare the stack that we will append to and pop to when it comes to each temp from the temperatures list
        # In order to output lengths betwee ntemps correctly, we will pair our numbers together in the stack like this -> [temp,index]
        stack = []
        
        for i, t in enumerate(temperatures):
            # Next step is to check if the stack is empty and if the temperature being added is greater than the on before it
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                answer[stackI] = [i - stackI]
            stack.append([t,i])
        return answer
        