from os import system


def print_message(lines, cls=False):
    if cls:
        system('clear')

    print('= ' * 30 + '\n')
    for line in lines:
        print(line)
    print()
