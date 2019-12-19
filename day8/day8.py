import numpy as np


def get_input():
    for line in open('input', 'r'):
        return line.replace('\n', '')


def get_layers(l, w, remainder, layers):

    if len(remainder) < l*w:
        return layers
    else:

        return get_layers(l, w, remainder[l*w:], layers + [remainder[:l*w]])


def num_c(layer, char):
    return sum([c == char for c in layer])


layers1 = get_layers(25, 6, get_input(), [])

target_layer = layers1[np.argmin([num_c(l, '0') for l in layers1])]

answer_part1 = num_c(target_layer, '1') * num_c(target_layer, '2')

print('answer part 1: {}'.format(answer_part1))


# part 2

def get_pixel_at(layers, i):

    for l in layers:
        if l[i] == '0':
            return ' '
        elif l[i] == '1':
            return '1'



def print_image(layers, length , width):
    for row_number in range(length):
        row = ''
        for column_number in range(width):
            row += get_pixel_at(layers, row_number * width + column_number)

        print(row)


print_image(layers1, 6, 25)
