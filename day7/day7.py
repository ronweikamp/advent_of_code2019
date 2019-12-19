from day5 import run


def get_init_state():
    for line in open('input', 'r'):
        return [int(l) for l in line.split(',')]


def run_phase_setting(code, phase_settings):

    input_output = 0

    for p in phase_settings:
        _, input_output = run(0, code, inputs=[p, input_output])

    return input_output
