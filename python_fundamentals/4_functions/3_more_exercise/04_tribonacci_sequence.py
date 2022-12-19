def tribonacci(n):
    sequence = [1, 1, 2]
    if n <= len(sequence):
        sequence = sequence[:n]
    else:
        for i in range(n-3):
            sequence.append(sum(sequence[i:i+3]))

    return ' '.join(str(x) for x in sequence)


print(tribonacci(int(input())))
