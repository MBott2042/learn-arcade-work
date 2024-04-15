import re

# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


some_names = ['DamianLoveless', 'Rufus Hades', 'Severin the Unpleasant']


def main():
    names = open("super_villains.txt")
    for name in names:
        name = name.strip()
        for some_name in some_names:
            if name == some_name:
                print('hey', name, 'matches')

    for some_name in some_names:
        for name in names:
            name = name.strip()
            if name == some_name:
                print('hey', name, 'matches')

    main()
