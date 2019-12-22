from day5 import run_get_outs


def run_with_mem(code):
    return run_get_outs(code + [0 for _ in range(1000)])


x = run_with_mem([109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99])

print(x)