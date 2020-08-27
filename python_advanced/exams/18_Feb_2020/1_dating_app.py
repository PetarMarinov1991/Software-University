from collections import deque


def convert_to_integers(my_input):
    return [int(x) for x in my_input.split()]


def matches_count(males_deque, females_deque, current_m, current_f):
    count = 0
    if males_deque and females_deque and current_m > 0 and current_f > 0:
        if current_m == current_f:
            males_deque.pop()
            count += 1
        else:
            males_deque.append(males_deque.pop() - 2)
        females_deque.popleft()
    return count


def check_conditions(my_key, my_value, males_deque, females_deque):
    if my_value <= 0:
        males_deque.pop() if my_key == 'm' else females_deque.popleft()
    elif my_value % 25 == 0:
        males_deque.pop() if my_key == 'm' else females_deque.popleft()
        if males_deque and my_key == 'm':
            males_deque.pop()
        elif females_deque and my_key == 'f':
            females_deque.popleft()


def output_people_left(males_deque, females_deque):
    output = ''
    genders = {'Males': males_deque, 'Females': females_deque}
    for k, _ in genders.items():
        if k == 'Males':
            collection = males_deque
        else:
            collection = females_deque
        output += f'{k} left: {", ".join([str(x) for x in collection])}\n' if collection else f'{k} left: none\n'
    return output


males = deque(convert_to_integers(input()))
females = deque(convert_to_integers(input()))
matches = 0

while males and females:
    current_male = males[-1]
    current_female = females[0]
    for key, value in {'m': current_male, 'f': current_female}.items():
        check_conditions(key, value, males, females)
    matches += matches_count(males, females, current_male, current_female)

print(f'Matches: {matches}')
print(output_people_left(males, females))
