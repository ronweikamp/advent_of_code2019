import itertools
import numpy as np

def get_init_state():
    with open('test_input2', 'r') as f:
        state = []
        for line in f:
            line = line.replace('=', '')
            line = line.replace('x', '')
            line = line.replace('y', '')
            line = line.replace('z', '')
            line = line.replace('<', '')
            line = line.replace('>', '')
            state.append(np.array([int(l) for l in line.split(',')]))

        return state


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
    last_velocity = [(0, 0, 0) for _ in range(n_moons)]

    while True:

        # calc velocity
        velocity_delta = [(0, 0, 0) for _ in range(n_moons)]
        for moon1 in range(n_moons):
            for moon2 in range(n_moons):
                if moon1 != moon2:
                    delta_v = calc_velocity_delta(last_position[moon1], last_position[moon2])
                    velocity_delta[moon1] = np.add(velocity_delta[moon1], delta_v)

        new_v = [np.add(last_velocity[i], velocity_delta[i]) for i in range(n_moons)]

        new_p = [np.add(last_position[i], new_v[i]) for i in range(n_moons)]

        last_position = new_p
        last_velocity = new_v

        yield new_p, new_v


def system_energy(p, v):
    total = 0

    for i in range(len(p)):
        total += sum([abs(e) for e in p[i]]) * sum([abs(e) for e in v[i]])
    return total


init_state = get_init_state()

print(init_state)
g = system_generator(init_state)

# for i in range(10):
#     print(system_energy(*next(g)))

count = 0
# print(np.equal(init_state, next(g)))
while True:
    # print(np.sum((np.equal(init_state, next(g)))))
    if np.sum(np.equal(init_state, next(g)[0])) == 12:

        print(count + 2)
        break
    if count % 10000 ==0:
        print(count)
    count += 1