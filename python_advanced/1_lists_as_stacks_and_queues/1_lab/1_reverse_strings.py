original_string = input()

stack = [ch for ch in original_string]
reversed_string = ''

while stack:
    reversed_string += stack.pop()

print(reversed_string)
