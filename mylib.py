import numpy as np


def recognize_pattern(pattern, patterns):
    matched_char = None
    most_common = 0
    match_acc = 0
    # print_pattern(pattern)
    # print(pattern)
    # input()
    for char, chars_patterns in patterns.items():
        for char_pattern in chars_patterns:
            common = 0
            for item in pattern:
                if item in char_pattern:
                    common += 1

            if common > most_common:
                most_common = common
                match_acc = common / len(char_pattern)
                matched_char = char
            # if match_acc > 0.97:
            #     return match_acc, matched_char
    return match_acc, matched_char


def print_pattern(pattern):
    size = 20
    print("=" * 22)
    for i in range(size):
        print("|", end="")
        for j in range(size):
            if (j, i) in pattern:
                print("X", end="")
            else:
                print(" ", end="")
        print("|")
    print("=" * 22)
