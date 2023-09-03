target = 12
pos = [10,8,0,5,3]
speed = [2,4,1,1,3]

pair = [(p, s) for p, s in zip(pos, speed)] # So we grab each pair of position and speed
pair.sort(reverse=True) # we then sort the array and reverse it --- we reverse it because we want the greatest position first... this is because we want the positions closest to the target as they will be our first carfleets considering their speeds
stack = [] # we declare an empty stack --- this will allow us to grab the first paired value and see if the next one closest is going to reach the destination at the same time as the one before it


for p,s in pair:
    stack.append((target - p) / s)
    if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()
        print(stack)
print(stack)

