def solve_captcha(game):
    empty_spaces = []
    balls = {'1': [], '2': [], '3': [], '4': []}
    for i, row in enumerate(game):
        for j, cell in enumerate(row):
            if cell == 0:
                empty_spaces.append((i, j))
            elif str(cell) in balls:
                balls[str(cell)].append((i, j))

    for ball_type, positions in balls.items():
        for position in positions:
            for empty_space in empty_spaces:
                new_game = [r[:] for r in game]
                new_game[position[0]][position[1]] = 0
                new_game[empty_space[0]][empty_space[1]] = int(
                    ball_type)

                if is_solved(new_game, int(ball_type)):
                    return [list(position), list(empty_space)]

    return None


def is_solved(game, ball_type):
    for row in game:
        if row.count(ball_type) == 5:
            return True

    for j in range(len(game[0])):
        column = [game[i][j] for i in range(len(game))]
        if column.count(ball_type) == 5:
            return True

    if [game[i][i] for i in range(len(game))].count(ball_type) == 5:
        return True

    if [game[i][len(game)-1-i] for i in range(len(game))].count(ball_type) == 5:
        return True

    return False