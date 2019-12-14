
operations = {
    'R': lambda x, y: (x + 1, y),
    'U': lambda x, y: (x, y + 1),
    'L': lambda x, y: (x - 1, y),
    'D': lambda x, y: (x, y - 1)
}

def coords_from_path(directions):

    x = 0
    y = 0

    coords = set()

    for d in directions:
        for i in range(1, int(d[1:]) + 1):
            x, y = operations[d[0]](x, y)
            coords.add((x, y))

    return coords


def get_intersections(path1, path2):
    return coords_from_path(path1).intersection(coords_from_path(path2))


def get_manhattan(path1, path2):
    return min([abs(t[0]) + abs(t[1]) for t in get_intersections(path1, path2)])


def get_num_steps_to_coord(path, coord):
    x = 0
    y = 0

    steps = 0
    for d in path:
        for i in range(1, int(d[1:]) + 1):
            x, y = operations[d[0]](x, y)
            steps += 1
            if (x, y) == coord:
                return steps


def get_min_distance(path1, path2):
    distances = []

    for c in get_intersections(path1, path2):
        d1 = get_num_steps_to_coord(path1, c)
        d2 = get_num_steps_to_coord(path2, c)
        distances.append(d1 + d2)

    return min(distances)


lines = []
for line in open('input', 'r'):
    lines.append(line.split(','))

print(get_manhattan(lines[0], lines[1]))
print(get_min_distance(lines[0], lines[1]))

