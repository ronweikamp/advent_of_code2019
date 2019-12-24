from day5 import run

def get_init_state():
    with open('input', 'r') as f:
        for line in f:
            return [int(l) for l in line.split(',')]


rotate = {
    'north': lambda r: 'east' if r else 'west',
    'west': lambda r: 'north' if r else 'south',
    'east': lambda r: 'south' if r else 'north',
    'south': lambda r: 'west' if r else 'east'
}

move = {
    'north': lambda x, y: (x, y + 1),
    'west': lambda x, y: (x - 1, y),
    'east': lambda x, y: (x + 1, y),
    'south': lambda x, y: (x, y - 1)
}

# g = run(0, get_init_state() + [0] * 1000, inputs=[0])
#
# colored = dict()
# position = (0, 0)
# orientation = 'north'
# return_code = -1
#
# while return_code != 0:
#
#     _, color, _, return_code = next(g)
#
#     if return_code == 0:
#         break
#
#     code, rotation, index, return_code = next(g)
#
#     if color:
#         colored[position] = 1
#     else:
#         if position in colored:
#             colored[position] = 0
#
#     orientation = rotate[orientation](rotation)
#     position = move[orientation](*position)
#
#     current_color = colored[position] if position in colored else 0
#
#     g = run(index, code, inputs=[current_color])
#
#
# print(len(colored))


# part 2

g = run(0, get_init_state() + [0] * 1000, inputs=[1])

colored = {(0, 0): 1}
position = (0, 0)
orientation = 'north'
return_code = -1

while return_code != 0:

    _, color, _, _, return_code = next(g)

    if return_code == 0:
        break

    code, rotation, index, relative_base, return_code = next(g)

    if color:
        colored[position] = 1
    else:
        if position in colored:
            colored[position] = 0

    orientation = rotate[orientation](rotation)
    position = move[orientation](*position)

    current_color = colored[position] if position in colored else 0

    g = run(index, code, inputs=[current_color], relative_base=relative_base)


print(colored)

for y in reversed([-5, -4,-3,-2,-1, 0]):
    line = ''
    for x in range(40):
        p = (x, y)
        if p in colored and colored[p]:
            line += 'x'
        else:
            line += ' '
    print(line)