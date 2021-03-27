INDENTS = 4


def print_hanging_indents(poem):
    first_line = True
    for line in poem.strip().splitlines():
        if first_line:
            print(line.strip())
            first_line = False
        elif line == '':
            first_line = True
        else:
            print(f'{INDENTS * " "}{line.lstrip()}')
