from day15 import new_position

def get_map():
    the_map = dict()
    with open('the_map', 'r') as f:
        y = 0
        for line in f:
            x = 0
            line = line.replace('\n', '')[4:]

            for c in line:
                the_map[(x, y)] = c
                x += 1

            y += 1

    return the_map




def num_vacuum(the_map):
    return len([v for v in the_map.values() if v == ' '])


def contains_no_vacuum(the_map):
    return num_vacuum(the_map) == 0


def find_oxygen_positions(the_map):
    return [key for key, value in the_map.items() if value == 'O']


def find_vacuum_next_to(position, the_map):
    positions = []

    n = new_position(position, 'north')
    w = new_position(position, 'west')
    e = new_position(position, 'east')
    s = new_position(position, 'south')

    for p in [n, w, e, s]:
        if p in the_map and the_map[p] == ' ':
            positions.append(p)

    return positions


the_map = get_map()

print(contains_no_vacuum(the_map))
count = 0

while not contains_no_vacuum(the_map):
    print('minutes {}'.format(count))
    print('num vacuum {}'.format(num_vacuum(the_map)))

    for op in find_oxygen_positions(the_map):
        for v in find_vacuum_next_to(op, the_map):
            the_map[v] = 'O'

    count += 1




# print(next(key for key, value in the_map.items() if value == 'O'))
