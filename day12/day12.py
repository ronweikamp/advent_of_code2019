import itertools
import numpy as np

def get_init_state():
    with open('input', 'r') as f:
        state = []
        for line in f:
            line = line.replace('=', '')
            line = line.replace('x', '')
            line = line.replace('y', '')
            line = line.replace('z', '')
            line = line.replace('<', '')
            line = line.replace('>', '')
            state.append(np.array([int(l) for l in line.split(',')]))

        return np.array(state)


def calc_velocity_delta(position1, position2):
    vd = [0 for _ in range(3)]

    for i in range(3):
        if position1[i] < position2[i]:
            vd[i] += 1
        elif position1[i] > position2[i]:
            vd[i] -= 1

    return vd


def system_generator(position_state):

    n_moons = len(position_state)

    last_position = position_state
    last_velocity = np.zeros([4,3])

    while True:

        # calc velocity
        # velocity_delta = [(0, 0, 0) for _ in range(n_moons)]
        for moon1 in range(n_moons):
            for moon2 in range(moon1 + 1, n_moons):
                for i in range(3):
                    if last_position[moon1][i] < last_position[moon2][i]:
                        last_velocity[moon1][i] += 1
                        last_velocity[moon2][i] -= 1
                    elif last_position[moon1][i] > last_position[moon2][i]:
                        last_velocity[moon1][i] -= 1
                        last_velocity[moon2][i] += 1

        # new_v = [np.add(last_velocity[i], velocity_delta[i]) for i in range(n_moons)]

        # new_p = [np.add(last_position[i], new_v[i]) for i in range(n_moons)]

        last_position = np.add(last_position, last_velocity)
        # last_velocity = new_v

        yield last_position, last_velocity


def system_energy(p, v):
    total = 0

    for i in range(len(p)):
        total += sum([abs(e) for e in p[i]]) * sum([abs(e) for e in v[i]])
    return total


init_state = get_init_state()

print(init_state)
g = system_generator(init_state)

# for i in range(100):
#     print(system_energy(*next(g)))

count = 1

checked = set()
counts = []

while True:

    new_position = next(g)

    for i in range(3):
        if i not in checked:
            if np.sum(np.equal(init_state[:, i], new_position[0][:, i])) == 4 and np.sum(np.abs(new_position[1][:, i])) == 0:
                print('dimension {}'.format(i))
                print('velocity {}'.format(new_position[1]))
                print('position {}'.format(new_position[0]))
                print('count {}'.format(count))
                counts.append(count)
                checked.add(i)

    if len(checked) == 3:
        break

    if count % 10000 == 0:
        print(count)
        # break

    count += 1

print(np.lcm.reduce(counts))
