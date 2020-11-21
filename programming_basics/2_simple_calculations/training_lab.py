w = float(input()) * 100
h = float(input()) * 100

w_space = int(w / 120)
h_space = int((h - 100) / 70)
seats_count = w_space * h_space - 3

print(seats_count)
