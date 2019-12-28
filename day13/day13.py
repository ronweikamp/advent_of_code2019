from day5 import run
import random
from collections import deque
import time

def get_init_state():
    with open('input', 'r') as f:
        for line in f:
            return [int(l) for l in line.split(',')]

def load_save_game():
    with open('save_game', 'r') as f:
        for line in f:
            line = line.replace('[', '')
            line = line.replace(']', '')
            return [int(l) for l in line.split(',')]


# part 1
g = run(0, get_init_state() + [0] * 1000, inputs=[])
tiles = [r[1] for r in g if r[-1] != 0]
print(sum([t_id == 2 for t_id in tiles[2::3]]))

# part 2


# display = []
# def get_score(outs):
#     i = outs.index(-1)
#     return outs[i+2]

# moves = []
# num_tiles_at_out = 344
# last_score = 0


# def find_max_score(display, generator, depth):
#     result_code = -1
#     outs = deque()
#
#     while result_code != 0:
#
#         code, out, index, relative_base, result_code = next(generator)
#         if result_code == 1:
#
#             while len(outs) > 2:
#                 x = outs.popleft()
#                 y = outs.popleft()
#                 t_id = outs.popleft()
#                 display[(x, y)] = t_id
#
#             return max([find_max_score(display.copy(), run(index, code, inputs=[-1], relative_base=relative_base), depth + 1),
#                         find_max_score(display.copy(), run(index, code, inputs=[0], relative_base=relative_base), depth + 1),
#                         find_max_score(display.copy(), run(index, code, inputs=[1], relative_base=relative_base), depth + 1)])
#
#         elif result_code == 2:
#             outs.append(out)
#
#     score = display[(-1,0)]
#     num_blocks = sum([t == 2 for t in display.values()])
#     print('num blocks {} score {} depth {}'.format(num_blocks, score, depth))
#     return score
#
#
init_state = get_init_state()
init_state[0] = 2

# save_game = load_save_game()
# print(load_save_game()[:-10])
g = run(0, init_state + [0] * 1000, inputs=[])
display = dict()

tiles = {
    0: ' ',
    1: '|',
    2: 'x',
    3: '=',
    4: '0'
}

ran = random.Random()

def print_display(display):
    x_min = min([x[0] for x in display.keys() if x[0] != -1])
    x_max = max([x[0] for x in display.keys() if x[0] != -1])
    y_min = min([x[1] for x in display.keys() if x[0] != -1])
    y_max = max([x[1] for x in display.keys() if x[0] != -1])

    print([x_min, x_max, y_min, y_max])

    for y in range(y_max):
        row = str(y).zfill(2)
        for x in range(x_max):
            row += tiles[display[(x,y)]]
        print(row)


    print('Score: {}'.format(display[(-1, 0)]))
    print('Blocks: {}'.format(sum([t == 2 for t in display.values()])))

outs = deque()
moves = []
# print(save_game)
result_code = -1

def find_ball(display):
    for k in display:
        if display[k] == 4:
            return k

def find_paddle(display):
    for k in display:
        if display[k] == 3:
            return k


# while result_code != 0:
#
#     code, out, index, relative_base, result_code = next(g)
#     if result_code == 1:
#
#         while len(outs) > 2:
#             x = outs.popleft()
#             y = outs.popleft()
#             t_id = outs.popleft()
#             display[(x, y)] = t_id
#
#         print(moves)
#         print_display(display)
#
#         print('Provide move: ')
#
#
#         # idea, if ball is on ground, rewrite history such that paddle is beneath ball on time
#         if find_ball(display)[1] == 21:
#             print_display(display)
#             paddle_x = (find_paddle(display))[0]
#             ball_x = (find_ball(display))[0]
#
#             diff = ball_x - paddle_x
#
#             moves = list(moves)
#             count = 0
#             print(diff)
#
#
#             r = 1
#
#             print('rand {}'.format(r))
#             if diff > 0:
#                 for i in range(0, 100):
#                     if moves[len(moves) - 1 - i] == 0:
#                         moves[len(moves) - 1 - i] = 1
#                         count += 1
#                     if count == diff:
#                         break
#             else:
#                 for i in range(0, 100):
#                     if moves[len(moves) - 1 - i] == 0:
#                         moves[len(moves) - 1 - i] = -1
#                         count += 1
#                     if count == abs(diff):
#                         break
#
#             print('rewriting')
#             print(len(moves))
#             s = time.time()
#             print('s')
#             g = run(0, init_state + [0] * 1000, inputs=list(moves))
#             print(time.time() - s)
#             code, out, index, relative_base, result_code = next(g)
#             outs.append(out)
#         else:
#             # do nothing
#             print_display(display)
#             move = 0
#             r = ran.randint(0, 1000)
#
#             # if r < 100:
#             #     move = 1
#             # elif 100 < r < 200:
#             #     move = -1
#
#             g = run(index, code, inputs=[move], relative_base=relative_base)
#             moves.append(move)
#
#         # if find_ball(display)[1] <= 14:
#         #     user_input = 0
#         #     g = run(index, code, inputs=[user_input], relative_base=relative_base)
#         #     moves.append(user_input)
#         # else:
#         #     user_input = int(input())
#         #     g = run(index, code, inputs=[user_input], relative_base=relative_base)
#         #     moves.append(user_input)
#
#
#     elif result_code == 2:
#         outs.append(out)

# idea above: if ball is on ground, rewrite history such that paddle is beneath ball on time, this gets stuck in a loop,
# don't know why but others report similar behavior with this strategy. Below works

# idea: move paddle according to x position of ball, this works
while result_code != 0:

    code, out, index, relative_base, result_code = next(g)

    if result_code == 1:

        while len(outs) > 2:
            x = outs.popleft()
            y = outs.popleft()
            t_id = outs.popleft()
            display[(x, y)] = t_id

        print(moves)

        paddle_x = (find_paddle(display))[0]
        ball_x = (find_ball(display))[0]
        print_display(display)

        print('Provide move: ')

        move = 0

        if paddle_x > ball_x:
            move = -1
        elif paddle_x < ball_x:
            move = 1

        g = run(index, code, inputs=[move], relative_base=relative_base)
        moves.append(move)
    elif result_code == 2:
        outs.append(out)
    else:
        while len(outs) > 2:
            x = outs.popleft()
            y = outs.popleft()
            t_id = outs.popleft()
            display[(x, y)] = t_id

        print_display(display)

print(moves)