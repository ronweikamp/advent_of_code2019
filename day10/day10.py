
# given coord 1 and coord 2, which grid coords are inbetween the line crossing 1 and 2?
# (x1 ,y1) ; (x2, y2)
# points (x,y) such that x1 <= x <= x2 and such that angle is the same, dx/dy is same

import math

def get_coords():
    coords = set()
    with open('input', 'r') as f:
        y = 0
        for line in f:
            line = line.replace('\n', '')
            x = 0
            for c in line:
                if c == '#':
                    coords.add((x, y))

                x += 1

            y += 1

    return coords


def angle_x(coord1, coord2):
    return math.atan2(coord2[1] - coord1[1], coord2[0] - coord1[0])

def angle_y(coord1, coord2):
    return math.atan2(coord2[0] - coord1[0], - coord2[1] + coord1[1])

def my_ordering(coord1, coord2):
    a = angle_y(coord1, coord2)

    if a >= 0:
        return a
    else:
        return 2 * math.pi + a


def coords_inbetween(coord1, coord2):

    a = angle_x(coord1, coord2)

    min_x = min([coord1[0], coord2[0]])
    max_x = max([coord1[0], coord2[0]])
    min_y = min([coord1[1], coord2[1]])
    max_y = max([coord1[1], coord2[1]])

    result = set()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            coord = (x, y)
            if coord != coord1 and coord != coord2:
                if angle_x(coord1, coord) == a:
                    result.add(coord)

    return result


asteroids = get_coords()

asteroids_to_los = {a:0 for a in asteroids}

for a in asteroids:
    for b in asteroids:
        if not b == a:
            if len(coords_inbetween(a, b).intersection(asteroids)) == 0:
                asteroids_to_los[a] += 1


print(max(asteroids_to_los.values()))


# part 2
for a in asteroids_to_los:
    if asteroids_to_los[a] == max(asteroids_to_los.values()):
        print(a)

location = (26, 29)

print(len(asteroids))

sorted_angles = sorted(list(set([my_ordering(location, a) for a in asteroids if a != location])))

print(len(sorted_angles))

angle_to_asteroid = dict()

def distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) ** 2 + abs(coord1[1] - coord2[1]) ** 2

for a in asteroids:

    ordering = my_ordering(location, a)

    if ordering not in angle_to_asteroid:
        angle_to_asteroid[ordering] = []

    angle_to_asteroid[ordering].append(a)

print(len(angle_to_asteroid))

for a in sorted_angles:
    angle_to_asteroid[a] = sorted(angle_to_asteroid[a], key=lambda a: distance(location, a))
    # print(angle_to_asteroid[a])


count = 1
for a in sorted_angles:
    if len(angle_to_asteroid[a]) > 0:
        if count == 200:
            print(angle_to_asteroid[a].pop(0))
        count += 1




# print(angle_x((2, 2), (2, 1)))
# print(angle_x((2, 2), (2, 0)))
# print(angle_x((2, 2), (2, 4)))
# print(angle_x((2, 2), (1, 1)))
#
# print(my_ordering((2, 2), (2, 1)))
# print(my_ordering((2, 2), (2, 0)))
# print(my_ordering((2, 2), (1, 4)))
# print(my_ordering((2, 2), (1, 1)))
# print(my_ordering((2, 2), (1, 0)))
#
# print(2 * math.pi)
