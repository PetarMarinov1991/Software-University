from collections import deque

rows, cols = input().split()
string = deque(input())
matrix = [[] for _ in range(int(rows))]

for i in range(len(matrix)):
    while len(matrix[i]) < int(cols):
        current_char = string.popleft()
        matrix[i].append(current_char)
        string.append(current_char)
    output = ''.join(matrix[i])
    print(output[::-1] if i % 2 != 0 else output)
