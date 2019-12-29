from day5 import run
import random

def get_init_state():
    with open('input', 'r') as f:
        for line in f:
            return [int(l) for l in line.split(',')]


directions = {
    'north': 1,
    'south': 2,
    'west': 3,
    'east': 4
}


def num_to_direction(num):
    return next(key for key, value in directions.items() if value == num)


def rotate(rand):
    r = rand.random()

    if r < 0.5:
        return ['south', 'east'][rand.randint(0, 1)]
    else:
        return ['north', 'west'][rand.randint(0, 1)]

    # return num_to_direction(rand.randint(1,4))

def new_position(current_position, direction):
    return {
        'north': lambda c: (c[0], c[1] + 1),
        'south': lambda c: (c[0], c[1] - 1),
        'west': lambda c: (c[0] - 1, c[1]),
        'east': lambda c: (c[0] + 1, c[1])
    }[direction](current_position)



def print_map(the_map):
    tiles = {
        0: 'x',
        1: ' ',
        2: '$'
    }

    x_min = min([x[0] for x in the_map.keys()])
    x_max = max([x[0] for x in the_map.keys()])
    y_min = min([x[1] for x in the_map.keys()])
    y_max = max([x[1] for x in the_map.keys()])

    print([x_min, x_max, y_min, y_max])

    for y in reversed(range(y_min, y_max + 1)):
        row = str(y).zfill(3)
        for x in range(x_min - 1, x_max + 1):
            if (x, y) in the_map:
                row += tiles[the_map[(x,y)]]
            else:
                row += '?'
        print(row)


    row = '   '
    for x in range(x_min - 1, x_max + 1):
        if x < 0:
            row += str(abs(x % -10))
        else:
            row += str(x % 10)

    print(row)

if __name__ == '__main__':
    rotations = {
        'north': 'west',
        'south': 'east',
        'west': 'south',
        'east': 'north'
    }

    init_state = get_init_state()
    current_position = (0, 0)

    the_map = dict()
    the_map[(0, 0)] = 1  # not wall

    current_direction = 'west'

    g = run(0, init_state, inputs=[directions[current_direction]])

    rand = random.Random()

    while True:

        code, out, index, relative_base, return_code = next(g)

        new_p = new_position(current_position, current_direction)

        if out == 0:
            the_map[new_p] = 0
            # wall, rotate
            current_direction = rotate(rand)
        elif out == 1:
            the_map[new_p] = 1
            current_position = new_p
            current_direction = rotate(rand)
        elif out == 2:
            the_map[new_p] = 2
            current_position = new_p
            print('Found oxygen system at {}'.format(current_position))
            break

        g = run(index, code, inputs=[directions[current_direction]], relative_base=relative_base)


        print(len(the_map))
        print('pos {} dir {}'.format(current_position, current_direction))

        print_map(the_map)




