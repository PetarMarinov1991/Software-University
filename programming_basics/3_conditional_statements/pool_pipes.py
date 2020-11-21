v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_work = p1 * h
p2_work = p2 * h
total_work = p1_work + p2_work
total_percent = total_work / v * 100
p1_percent = p1_work / total_work * 100
p2_percent = p2_work / total_work * 100

diff = total_work - v
if diff > 0:
    print(f'For {h:.2f} hours the pool overflows with {diff:.2f} liters.')
else:
    print(f'The pool is {total_percent:.2f}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%."')