from os import system


def clear():
    system('clear')


def print_message(lines, cls=False):
    if cls:
        clear()
    print("= " * 30 + '\n')
    for line in lines:
        print(line)
    print()
