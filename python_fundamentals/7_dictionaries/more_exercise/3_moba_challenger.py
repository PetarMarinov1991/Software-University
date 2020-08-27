def sort_dict(my_dict):
    my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))}
    return my_dict


pool = dict()

while True:
    line = input()

    if line == 'Season end':
        break

    if ' -> ' in line:
        line = line.split(' -> ')
        player, pos, skill = line[0], line[1], int(line[2])
        if player not in pool:
            pool.update({player: {pos: skill}})
        elif pos not in pool[player]:
            pool[player].update({pos: skill})
        elif pool[player][pos] < skill:
            pool[player][pos] = skill
    else:
        line = line.split(' vs ')
        player_1, player_2 = line[0], line[1]
        to_remove = []
        if player_1 in pool and player_2 in pool:
            for player, pos in pool.items():
                for current_pos in pos:
                    if pool[player_1].__contains__(current_pos) and pool[player_2].__contains__(current_pos):
                        if pool[player_1][current_pos] > pool[player_2][current_pos]:
                            to_remove.append(player_2)
                        elif pool[player_2][current_pos] > pool[player_1][current_pos]:
                            to_remove.append(player_1)
            for player in set(to_remove):
                del pool[player]

total_skill = dict()

for player, info in pool.items():
    total_skill.update({player: 0})
    for pos, skill in info.items():
        total_skill[player] += skill

for player, skill in sort_dict(total_skill).items():
    print(f'{player}: {skill} skill')
    for pos, pos_skill in sort_dict(pool[player]).items():
        print(f'- {pos} <::> {pos_skill}')
