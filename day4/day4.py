def contains_adjacent(number):
    if len(str(number)) <= 1:
        return False

    elts = [int(s) for s in str(number)]

    return any(map(lambda t: t[0] == t[1], zip(elts, elts[1:])))


groups_to_remove = set([3 * str(i) for i in range(10)] + [4 * str(i) for i in range(10)])
groups_of_five = set([5 * str(i) for i in range(10)])

def contains_adjacent_not_part_of_larger_group(number):
    number_string = str(number)

    # if group contains group of five, it cannot contain adjacent
    for group in groups_of_five:
        if group in number_string:
            return False

    # remove groups of three and four, observe the rest
    for group in groups_to_remove:
        if group in number_string:
            rests = number_string.split(group)  # substrings that might contain adjacent pair
            rests = list(filter(lambda r: r not in groups_to_remove, rests))  # filter on rests that are not part of groups to remove

            # print(rests, any(map(lambda rest: contains_adjacent(rest), rests)))
            return any(map(lambda rest: contains_adjacent(rest), rests))

    return contains_adjacent(int(number_string))



def is_non_decreasing(number):
    elts = [int(s) for s in str(number)]

    return all(map(lambda t: t[0] <= t[1], zip(elts, elts[1:])))


def meets_criteria1(number):
    criteria = [contains_adjacent, is_non_decreasing]
    return all(map(lambda c: c(number), criteria))

def meets_criteria2(number):
    criteria = [contains_adjacent_not_part_of_larger_group, is_non_decreasing]
    return all(map(lambda c: c(number), criteria))


# print(sum([meets_criteria1(number) for number in range(240920, 789857)]))
# print(sum([meets_criteria2(number) for number in range(240920, 789857)]))

