def is_valid(pos, size):
    return pos[0] in range(size) and pos[1] in range(size)


def get_removed_knights(r, c, size, my_board):
    removed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        current_pos = [r + rows[i], c + cols[i]]
        if is_valid(current_pos, size) and my_board[current_pos[0]][current_pos[1]] == "K":
            removed_knights += 1
    return removed_knights


n = int(input())
board = [[x for x in input()] for _ in range(n)]
total_kills = 0

while True:
    most_kills = 0
    to_kill = []

    for row in range(n):
        for col in range(n):
            if board[row][col] == "K":
                killed_knights = get_removed_knights(row, col, n, board)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [row, col]

    if most_kills == 0:
        break

    board[to_kill[0]][to_kill[1]] = "0"
    total_kills += 1

print(total_kills)
