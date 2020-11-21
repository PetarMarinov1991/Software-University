from math import floor as fl

player_name = input()
games_played = int(input())

volleyball_games = 0
tennis_games = 0
badminton_games = 0

volleyball_score = 0
tennis_score = 0
badminton_score = 0

for i in range(games_played):
    game_name = input()
    score = int(input())

    if game_name == 'volleyball':
        volleyball_games += 1
        score *= 1.07
        volleyball_score += score

    elif game_name == 'tennis':
        tennis_games += 1
        score *= 1.05
        tennis_score += score

    elif game_name == 'badminton':
        badminton_games += 1
        score *= 1.02
        badminton_score += score

average_volleyball_score = fl(volleyball_score / volleyball_games)
average_tennis_score = fl(tennis_score / tennis_games)
average_badminton_score = fl(badminton_score / badminton_games)
total_score = fl(volleyball_score + tennis_score + badminton_score)

if average_volleyball_score >= 75 and average_tennis_score >= 75 and average_badminton_score >= 75:
    print(f'Congratulations, {player_name}! You won the cruise games with {total_score} points.')
else:
    print(f'Sorry, {player_name}, you lost. Your points are only {total_score}.')
