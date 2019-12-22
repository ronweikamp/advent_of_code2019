from day5 import run
import itertools

def get_init_state():
    with open('input', 'r') as f:
        for line in f:
            return [int(l) for l in line.split(',')]


def run_phase_setting(code, phase_settings):

    input_output = 0

    for p in phase_settings:
        _, input_output, _, _ = next(run(0, code, inputs=[p, input_output]))

    return input_output

def find_largest_out():

    code = get_init_state()

    largest = 0

    for setting in itertools.permutations([0, 1, 2, 3, 4]):
        out = run_phase_setting(code, setting)

        if out > largest:
            largest = out

    return largest

print('largest setting {}'.format(find_largest_out()))

# part 2

def run_feedbackloop_setting(code, phase_settings):

    amps = [code.copy() for _ in range(5)]
    indices = [0 for _ in range(5)]

    for i in range(5):
        print('amp {} phase {}'.format(i, phase_settings[i]))
        amps[i], input_output, indices[i], reason = next(run(indices[i], amps[i], inputs=[phase_settings[i]]))
        print('out {} reason {}'.format(input_output, reason))

    not_halted = True

    input_output = 0

    while not_halted:
        for i in range(5):
            amps[i], new_input_output, indices[i], reason = next(run(indices[i], amps[i], inputs=[input_output]))
            print('out {} reason {}'.format(input_output, reason))

            not_halted = reason is not 0

            if not_halted:
                input_output = new_input_output

    return input_output


def find_largest_out_feedback():

    code = get_init_state()

    largest = 0

    for setting in itertools.permutations([5, 6, 7, 8, 9]):
        out = run_feedbackloop_setting(code, setting)

        if out > largest:
            largest = out

    return largest


print(find_largest_out_feedback())
