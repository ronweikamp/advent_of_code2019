from day5 import run
import itertools

def get_init_state():
    for line in open('input', 'r'):
        return [int(l) for l in line.split(',')]


def run_phase_setting(code, phase_settings):

    input_output = 0

    for p in phase_settings:
        _, input_output = run(0, code, inputs=[p, input_output])

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
