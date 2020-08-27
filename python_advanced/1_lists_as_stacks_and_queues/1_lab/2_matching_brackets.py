expression = input()

stack = []
result = []

for idx in range(len(expression)):
    char = expression[idx]
    if expression[idx] == '(':
        stack.append(idx)
    elif expression[idx] == ')':
        start_idx = stack.pop()
        result.append(expression[start_idx:idx + 1])

[print(x) for x in result]
