import math
import random
import time
from collections import deque


def get_init_state(filename):
    chemical_to_req = dict()

    with open(filename, 'r') as f:

        for line in f:
            line = line.replace('\n', '')
            line = line.replace(',', '')
            a, b = (line.split('=>'))

            chemicals = (a.split(' ')[:-1][1::2])
            numbers = (a.split(' ')[:-1][::2])

            requirements = dict.fromkeys(chemicals)

            for i in range(len(chemicals)):
                requirements[chemicals[i]] = int(numbers[i])


            n, c = b.split(' ')[1:]
            chemical_to_req[c] = (int(n), requirements)

    return chemical_to_req


def calc_requirements(target, quantity, rlist):
    q, reqs = rlist[target]

    multiplier = math.ceil(quantity / q)
    return {c: multiplier * reqs[c] for c in reqs}


def contains_ORE_only(stack):
    return all(map(lambda t: t[0] == 'ORE', stack))


def merge_stack(stack):
    chemicals = set([t[0] for t in stack])

    if len(chemicals) < len(stack):
        new_stack = deque()
        for c in chemicals:
            new_stack.append((c, sum([t[1] for t in stack if t[0] == c])))
        stack = new_stack

    return stack


def calc_leftovers(chemical, quantity, rlist):
    if chemical == 'ORE':
        return 100000000

    q = rlist[chemical][0]
    return math.ceil(quantity / q) * q - quantity

def apply_leftovers(stack, leftovers):

    if len(leftovers) > 0:
        new_stack = deque()

        for c, q in stack:
            if c in leftovers:

                if q > leftovers[c]:
                    new_stack.append((c, q - leftovers[c]))
                    leftovers.pop(c)
                elif q == leftovers[c]:
                    leftovers.pop(c)
                else:
                    leftovers[c] -= q
            else:
                new_stack.append((c, q))

        stack = new_stack

    return stack


def sample_from_stack(stack, rand, reaction_list):

    leftovers = [calc_leftovers(t[0], t[1], reaction_list) for t in stack]
    min_left = min(leftovers)

    # if(min_left) > 0:
    #     print(min_left)
    # print(stack)

    indices = [l[1] for l in zip(leftovers, range(len(leftovers))) if l[0] == min_left]

    i = indices[rand.randint(0, len(indices) - 1)]
    stack.rotate(-i)

    return stack.popleft(), stack


def min_ORE_needed(reaction_list, fuel):
    stack = deque([("FUEL", fuel)])

    rand = random.Random()
    lefts = dict()

    while not contains_ORE_only(stack):
        stack = merge_stack(stack)
        stack = apply_leftovers(stack, lefts)

        e, stack = sample_from_stack(stack, rand, reaction_list)
        c = e[0]
        q = e[1]

        if c == 'ORE':
            stack.append((c, q))
            continue

        l = calc_leftovers(c, q, reaction_list)
        if l > 0:
            if c in lefts:
                lefts[c] += l
            else:
                lefts[c] = l

        for item in calc_requirements(c, q, reaction_list).items():
            stack.append(item)

    return merge_stack(stack)[0][1]


s = time.time()
# print(min_ORE_needed_search('test_input', 1))
print(min_ORE_needed(get_init_state('input'), 1))
print(time.time() - s)
