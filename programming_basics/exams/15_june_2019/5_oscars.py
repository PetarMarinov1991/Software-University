actor_name = input()
academy_points = float(input())
judges_count = int(input())

for judges in range(judges_count):
    judge_name = input()
    given_points = float(input())

    judge_points = (len(judge_name) * given_points) / 2
    academy_points += judge_points

    if academy_points >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
        exit(0)

print(f'Sorry, {actor_name} you need {1250.5 - academy_points:.1f} more!')
