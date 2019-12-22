from day5 import run_get_outs


def get_init_state():
    with open('input', 'r') as f:
        for line in f:
            return [int(l) for l in line.split(',')]


def run_with_mem(code, inputs=[]):

    return run_get_outs(code + [0 for _ in range(1000)], inputs=inputs)
