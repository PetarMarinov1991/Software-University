flock_of_sheep = input().split(', ')[::-1]

for i in range(len(flock_of_sheep)):
    animal = flock_of_sheep[i]
    if animal == 'wolf':
        if i == 0:
            print('Please go away and stop eating my sheep')
        else:
            print(f'Oi! Sheep number {i}! You are about to be eaten by a wolf!')
