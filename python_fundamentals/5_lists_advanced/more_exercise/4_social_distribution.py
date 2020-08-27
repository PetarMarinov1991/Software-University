import operator

population = list(map(int, input().split(', ')))
min_wealth = int(input())

for idx, person in enumerate(population):
    min_index, min_value = min(enumerate(population), key=operator.itemgetter(1))
    max_index, max_value = max(enumerate(population), key=operator.itemgetter(1))

    if min_value + min_wealth > max_value and (min_value + max_value) / 2 != min_wealth:
        population = None
        print('No equal distribution possible')
        break
    if person < min_wealth:
        population[idx] += min_wealth - person
        population[max_index] -= min_wealth - person

if population:
    print(population)
