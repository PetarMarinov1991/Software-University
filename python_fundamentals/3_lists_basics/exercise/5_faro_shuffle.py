cards = input().split()

half_deck = len(cards) // 2
first_half = cards[:half_deck]
second_half = cards[half_deck:]
result = []

shuffles = int(input())

for shuffle in range(shuffles):
    if shuffle > 0:
        result.clear()
    for i in range(half_deck):
        result.append(first_half[i])
        result.append(second_half[i])

    first_half = result[:half_deck]
    second_half = result[half_deck:]

print(result)
