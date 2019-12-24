instructions = {
    1: lambda code, index, relative_base, x, y, i: (code[:i] + [x + y] + code[i + 1:], index + 4, relative_base),
    2: lambda code, index, relative_base, x, y, i: (code[:i] + [x * y] + code[i + 1:], index + 4, relative_base),
    3: lambda code, index, relative_base, x, i: (code[:i] + [x] + code[i + 1:], index + 2, relative_base),
    4: lambda code, index, relative_base, x: (code, index + 2, relative_base),
    5: lambda code, index, relative_base, x, y: (code, y if x != 0 else index + 3, relative_base),
    6: lambda code, index, relative_base, x, y: (code, y if x == 0 else index + 3, relative_base),
    7: lambda code, index, relative_base, x, y, i: (
    code[:i] + [1] + code[i + 1:] if x < y else code[:i] + [0] + code[i + 1:], index + 4, relative_base),
    8: lambda code, index, relative_base, x, y, i: (
    code[:i] + [1] + code[i + 1:] if x == y else code[:i] + [0] + code[i + 1:], index + 4, relative_base),
    9: lambda code, index, relative_base, x: (code, index + 2, relative_base + x)
}

opcode_to_numparams = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 1,
    99: 0
}


def get_param(code, i, mode, relative_base):
    if mode == 1:  # 1 for immediate mode
        return i
    elif mode == 2:  # relative mode
        return code[i + relative_base]
    else:  # position mode
        return code[i]


def run_until_halt(index, code, inputs=[]):
    g = run(index, code, inputs)
    return [r for r in g][-1]


def run_until_halt_last_out(code, inputs=[]):
    return run_get_outs(code, inputs=inputs)[-1]


def run_get_outs(code, inputs=[]):
    g = run(0, code, inputs=inputs)
    return [r[1] for r in g if r[-1] == 2]


def run(index, code, inputs=[], relative_base=0):

    while True:

        param_opcode = str(code[index]).zfill(5)
        opcode = int(param_opcode[-2:])
        param_modes = [int(m) for m in reversed(param_opcode[:3])]
        numparams = opcode_to_numparams[opcode]
        params = [get_param(code, code[index + 1 + i], param_modes[i], relative_base) for i in range(numparams)]

        if opcode == 99:
            yield code, code[0], index, relative_base, 0
            return
        elif opcode == 3:

            if len(inputs) == 0:
                yield code, code[0], index, relative_base, 1

            destination = code[index + 1] + relative_base if param_modes[0] == 2 else code[index + 1]
            code, index, relative_base = instructions[3](code, index, relative_base, inputs.pop(0), destination)
        else:

            # if last is address, consider raw address
            if opcode in {1, 2, 3, 7, 8}:
                output_address = code[index + numparams]
                params[-1] = output_address + relative_base if param_modes[-1] == 2 else output_address

            # print(opcode)
            # print(param_opcode)
            code, index, relative_base = instructions[opcode](code, index, relative_base, *params)

            if opcode == 4:
                yield code, params[0], index, relative_base, 2


def main():

    init_state = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1, 192, 154, 224, 101, -161, 224, 224, 4, 224, 102, 8, 223, 223,
         101, 5, 224, 224, 1, 223, 224, 223, 1001, 157, 48, 224, 1001, 224, -61, 224, 4, 224, 102, 8, 223, 223, 101, 2, 224,
         224, 1, 223, 224, 223, 1102, 15, 28, 225, 1002, 162, 75, 224, 1001, 224, -600, 224, 4, 224, 1002, 223, 8, 223,
         1001, 224, 1, 224, 1, 224, 223, 223, 102, 32, 57, 224, 1001, 224, -480, 224, 4, 224, 102, 8, 223, 223, 101, 1, 224,
         224, 1, 224, 223, 223, 1101, 6, 23, 225, 1102, 15, 70, 224, 1001, 224, -1050, 224, 4, 224, 1002, 223, 8, 223, 101,
         5, 224, 224, 1, 224, 223, 223, 101, 53, 196, 224, 1001, 224, -63, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 3, 224,
         1, 224, 223, 223, 1101, 64, 94, 225, 1102, 13, 23, 225, 1101, 41, 8, 225, 2, 105, 187, 224, 1001, 224, -60, 224, 4,
         224, 1002, 223, 8, 223, 101, 6, 224, 224, 1, 224, 223, 223, 1101, 10, 23, 225, 1101, 16, 67, 225, 1101, 58, 10,
         225, 1101, 25, 34, 224, 1001, 224, -59, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 3, 224, 1, 223, 224, 223, 4,
         223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227,
         99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227,
         274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999,
         1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1108, 226, 226, 224,
         102, 2, 223, 223, 1005, 224, 329, 101, 1, 223, 223, 107, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 344, 1001,
         223, 1, 223, 107, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 359, 101, 1, 223, 223, 7, 677, 226, 224, 102, 2, 223,
         223, 1005, 224, 374, 101, 1, 223, 223, 108, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 389, 101, 1, 223, 223,
         1007, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 404, 101, 1, 223, 223, 7, 226, 677, 224, 102, 2, 223, 223, 1006,
         224, 419, 101, 1, 223, 223, 1107, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 434, 1001, 223, 1, 223, 1108, 226,
         677, 224, 102, 2, 223, 223, 1005, 224, 449, 101, 1, 223, 223, 108, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 464,
         1001, 223, 1, 223, 8, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 479, 1001, 223, 1, 223, 1007, 226, 226, 224,
         102, 2, 223, 223, 1006, 224, 494, 101, 1, 223, 223, 1008, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 509, 101, 1,
         223, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 524, 1001, 223, 1, 223, 108, 677, 677, 224, 1002, 223,
         2, 223, 1005, 224, 539, 1001, 223, 1, 223, 1107, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 554, 1001, 223, 1,
         223, 7, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 569, 1001, 223, 1, 223, 8, 677, 226, 224, 102, 2, 223, 223,
         1006, 224, 584, 101, 1, 223, 223, 1008, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 599, 101, 1, 223, 223, 1007,
         226, 677, 224, 1002, 223, 2, 223, 1006, 224, 614, 1001, 223, 1, 223, 8, 677, 677, 224, 1002, 223, 2, 223, 1005,
         224, 629, 101, 1, 223, 223, 107, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 644, 101, 1, 223, 223, 1108, 677, 226,
         224, 102, 2, 223, 223, 1005, 224, 659, 101, 1, 223, 223, 1008, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 674,
         1001, 223, 1, 223, 4, 223, 99, 226
         ]
    run(0, init_state, [1])
    run(0, init_state, [5])
    # input 1 => 11049715
    # input 5 => 2140710

    # print(run(0, [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
    #           1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
    #           999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]))

if __name__ == '__main__':
    main()