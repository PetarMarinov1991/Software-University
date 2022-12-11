deck = input().split()
shuffles = int(input())

half_deck = len(deck) // 2
# splits the deck in half from 2nd to last but one card to keep 1st and last in place
first_half = deck[1:half_deck]
second_half = deck[half_deck:-1]

new_deck = []

for _ in range(shuffles):
    new_deck.clear()

    for i in range(half_deck - 1):
        new_deck.append(second_half[i])
        new_deck.append(first_half[i])

    first_half = new_deck[:half_deck - 1]
    second_half = new_deck[half_deck - 1:]

new_deck = [deck[0]] + new_deck + [deck[-1]]
print(new_deck)
