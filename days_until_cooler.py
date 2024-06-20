def days_until_cooler(temps):
    result = [-1] * len(temps)
    stack = []
    temperature_stack = []
 
    for i in range(len(temps) - 1, -1, -1):
        # implement this
        while stack and temperature_stack[-1] >=  temps[i]:
            temperature_stack.pop()
            stack.pop()
        result[i] = (stack[-1] - i) if stack else  -1
        temperature_stack.append(temps[i])
        stack.append(i)
        
    
    return result

print(days_until_cooler([30, 60, 90, 120, 60, 30]))  # Expected: [-1, 4, 2, 1, 1, -1]
print(days_until_cooler([100, 95, 90, 85, 80, 75]))  # Expected: [1, 1, 1, 1, 1, -1]
print(days_until_cooler([1]))  # Expected: [-1]
