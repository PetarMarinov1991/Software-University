from collections import deque


def conditions(gifts):
    condition_1 = gifts['Bicycle'][1] > 0 and gifts['Teddy bear'][1] > 0
    condition_2 = gifts['Wooden train'][1] > 0 and gifts['Doll'][1] > 0
    if condition_1 or condition_2:
        return 'The presents are crafted! Merry Christmas!'
    return 'No presents this Christmas!'


def craft_gifts(boxes, magic, gifts):
    while boxes and magic:
        current_box = boxes.pop()
        current_magic = magic.popleft()
        if current_box == 0 and current_magic > 0:
            magic.insert(0, current_magic)
            continue
        elif current_magic == 0 and current_box > 0:
            boxes.append(current_box)
            continue
        prod = current_box * current_magic
        gift_crafted = False
        if prod > 0:
            for gift, value in gifts.items():
                if prod == value[0]:
                    value[1] += 1
                    gift_crafted = True
                    break
            if not gift_crafted:
                boxes.append(current_box + 15)
        elif prod < 0:
            diff = current_box + current_magic
            boxes.append(diff)

    print(conditions(gifts))

    if boxes:
        print(f'Materials left: {", ".join([str(x) for x in boxes][::-1])}')
    if magic:
        print(f'Magic left: {", ".join([str(x) for x in magic])}')

    return '\n'.join([f'{gift}: {value[1]}' for gift, value in sorted(gifts.items()) if value[1] > 0])


gifts_dict = {
    'Bicycle': [400, 0],
    'Teddy bear': [300, 0],
    'Wooden train': [250, 0],
    'Doll': [150, 0]
}
boxes_values = deque([int(x) for x in input().split()])
magic_values = deque([int(x) for x in input().split()])

print(craft_gifts(boxes_values, magic_values, gifts_dict))
