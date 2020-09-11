import random


def bankroll_and_steps(seq, starting_bet):
    sequence = [starting_bet, starting_bet]
    idx = 0
    for _ in range(seq - 2):
        sequence.append(sequence[idx] + sequence[idx + 1])
        idx += 1
    bankroll = sum(sequence)
    print(f'Bankroll: {bankroll}' + '\n' + f'Bets: {", ".join([str(x) for x in sequence])}' + '\n')
    return bankroll, sequence


def average_percentage_for_success(seq):
    average = []
    for _ in range(100):
        iteration_percentage = []
        for _ in range(100):
            result = [random.choice([1, 'X', 2]) for _ in range(seq)]
            if 'X' not in result:
                percentage = 0
            iteration_percentage.append(percentage)
            if 'X' in result:
                iteration_percentage.append(100)
            else:
                iteration_percentage.append(0)
        average.append(sum([x / 100 for x in iteration_percentage]))
    average = sum([x / 100 for x in average])
    return f'Percentage for success: {average:.2f}%'


def profit_per_step(seq):
    result = []
    seq = bankroll_and_steps(seq, bet)[1]
    coefficients = [3.00, 3.10, 3.20, 3.25, 3.30]
    for i in range(len(seq)):
        total_bet = sum(seq[:i + 1])
        profit = (seq[i] * random.choice(coefficients) - total_bet)
        result.append(f'Bet {i + 1} - Total bet: {total_bet}, +{profit:.2f}')
    return '\n'.join(result)


print('Input starting bet:')
bet = float(input())
print('Input positive integer:')
fib_sequence = int(input())

print(average_percentage_for_success(fib_sequence))
print(profit_per_step(fib_sequence))
