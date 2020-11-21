visitors = int(input())

workouts = ['Back', 'Chest', 'Legs', 'Abs']
proteins = ['Protein shake', 'Protein bar']

for _ in range(visitors):
    action = input()

    if action in workouts:
        workouts.append(action)

    elif action in proteins:
        proteins.append(action)

chest_workout = workouts.count('Chest') - 1
back_workout = workouts.count('Back') - 1
legs_workout = workouts.count('Legs') - 1
abs_workout = workouts.count('Abs') - 1
protein_shake = proteins.count('Protein shake') - 1
protein_bar = proteins.count('Protein bar') - 1
workout_visits = len(workouts) - 4
product_buy = len(proteins) - 2


percentage_workout_visitors = (workout_visits / visitors) * 100
percentage_protein_buyers = 100 - percentage_workout_visitors

print(f'{back_workout} - back')
print(f'{chest_workout} - chest')
print(f'{legs_workout} - legs')
print(f'{abs_workout} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{percentage_workout_visitors:.2f}% - work out')
print(f'{percentage_protein_buyers:.2f}% - protein')
