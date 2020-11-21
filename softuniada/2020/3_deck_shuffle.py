deck = list(range(1, int(input()) + 1))
indices = list(map(int, input().split()))

new_deck = []

for i in indices:
    first_half, second_half = deck[:i], deck[i:]

    while True:
        if first_half:
            new_deck.append(first_half.pop(0))
        if second_half:
            new_deck.append(second_half.pop(0))

        if len(new_deck) == len(deck):
            deck = new_deck
            new_deck = []
            break

print(' '.join(str(card) for card in deck))
