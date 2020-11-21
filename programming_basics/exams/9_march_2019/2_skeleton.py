minutes = int(input())
seconds = int(input())
length = float(input())
sec_per_100_m = int(input())

competition_in_seconds = minutes * 60 + seconds
time_reduced = length / 120
total_time_reduced = time_reduced * 2.5
marin_time = (length / 100) * sec_per_100_m - total_time_reduced

if competition_in_seconds >= marin_time:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {marin_time:.3f}.')
else:
    print(f'No, Marin failed! He was {marin_time - competition_in_seconds:.3f} second slower.')
