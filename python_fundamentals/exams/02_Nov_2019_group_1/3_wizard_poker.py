def valid_idx(index, my_list):
    if 0 <= index < len(my_list):
        return True


def valid_value(value, my_list):
    if value in my_list:
        return True


def swap_elements(elem_1, elem_2, my_list):
    idx_1, idx_2 = my_list.index(elem_1), my_list.index(elem_2)
    my_list[idx_1], my_list[idx_2] = my_list[idx_2], my_list[idx_1]


available_cards = input().split(':')

deck = []

while True:
    line = input().split()
    command = line[0]

    if command == 'Ready':
        break

    card = line[1]
    if command == 'Add':
        if valid_value(card, available_cards):
            deck.append(card)
        else:
            print('Card not found.')
    elif command == 'Insert':
        idx = int(line[2])
        if valid_value(card, available_cards) and valid_idx(idx, deck):
            deck.insert(idx, card)
        else:
            print('Error!')
    elif command == 'Remove':
        if valid_value(card, deck):
            deck.remove(card)
        else:
            print('Card not found.')
    elif command == 'Swap':
        card_2 = line[2]
        swap_elements(card, card_2, deck)
    elif command == 'Shuffle':
        deck = deck[::-1]

print(f'{" ".join(deck)}')
