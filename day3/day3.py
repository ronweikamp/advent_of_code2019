
operations = {
    'R': lambda x, y, step: (x + step, y),
    'U': lambda x, y, step: (x, y + step),
    'L': lambda x, y, step: (x - step, y),
    'D': lambda x, y, step: (x, y - step)
}

def coords_from_path(directions):

    x = 0
    y = 0

    coords = set()

    for d in directions:
        for i in range(1, int(d[1:]) + 1):
            x, y = operations[d[0]](x, y, 1)
            coords.add((x, y))

    return coords


def get_manhattan(path1, path2):
    return min([abs(t[0]) + abs(t[1]) for t in coords_from_path(path1).intersection(coords_from_path(path2))])

lines = []
for line in open('input', 'r'):
    lines.append(line.split(','))

print(get_manhattan(lines[0], lines[1]))

