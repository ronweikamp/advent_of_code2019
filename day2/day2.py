instructions = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y
}

# def run(code):

#     index = 0
#     running = True
#     while running:

#         opcode = code[index]

#         if opcode == 99:
#             return code
#         else:
#             code[code[index + 3]] = instructions[opcode](code[code[index + 1]], code[code[index + 2]])

#         index = (index + 4) % len(code)

#     return code

def run(index, code):
    if code[index] == 99:
        return code
    else:
        opcode = code[index]
        index_to_change = code[index + 3]
        new_value = instructions[opcode](code[code[index + 1]], code[code[index + 2]])
        new_code = code[:index_to_change] + [new_value] + code[index_to_change + 1:]
        new_index = (index + 4) % len(code)
        return run(new_index, new_code)


# answers
# [2, 0, 0, 0, 99]
# [2, 3, 0, 6, 99]
# [2, 4, 4, 5, 99, 9801]
# [30, 1, 1, 4, 2, 5, 6, 0, 99]

print(run(0, [1,0,0,0,99]))
print(run(0, [2,3,0,3,99]))
print(run(0, [2,4,4,5,99,0]))
print(run(0, [1,1,1,4,99,5,6,0,99]))

run(0, [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,1,31,5,35,1,9,35,39,2,13,39,43,1,43,10,47,1,47,13,51,2,10,51,55,1,55,5,59,1,59,5,63,1,63,13,67,1,13,67,71,1,71,10,75,1,6,75,79,1,6,79,83,2,10,83,87,1,87,5,91,1,5,91,95,2,95,10,99,1,9,99,103,1,103,13,107,2,10,107,111,2,13,111,115,1,6,115,119,1,119,10,123,2,9,123,127,2,127,9,131,1,131,10,135,1,135,2,139,1,10,139,0,99,2,0,14,0
])


def program(noun, verb):
    code = [1, noun, verb, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 5, 19, 23, 1, 23, 5, 27, 1, 27, 13,
            31, 1, 31, 5, 35, 1, 9, 35, 39, 2, 13, 39, 43, 1, 43, 10, 47, 1, 47, 13, 51, 2, 10, 51, 55, 1, 55, 5, 59, 1,
            59, 5, 63, 1, 63, 13, 67, 1, 13, 67, 71, 1, 71, 10, 75, 1, 6, 75, 79, 1, 6, 79, 83, 2, 10, 83, 87, 1, 87, 5,
            91, 1, 5, 91, 95, 2, 95, 10, 99, 1, 9, 99, 103, 1, 103, 13, 107, 2, 10, 107, 111, 2, 13, 111, 115, 1, 6,
            115, 119, 1, 119, 10, 123, 2, 9, 123, 127, 2, 127, 9, 131, 1, 131, 10, 135, 1, 135, 2, 139, 1, 10, 139, 0,
            99, 2, 0, 14, 0]

    return run(0, code)[0]

program(12,2)

# day_2_part_2
for noun in range(1,100):
    for verb in range(1,100):
        if program(noun, verb) == 19690720:
            print(100*noun + verb)