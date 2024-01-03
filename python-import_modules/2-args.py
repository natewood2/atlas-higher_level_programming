#!/usr/bin/python3

import sys

if __name__ == "__main__":
    arg_c = len(sys.argv) - 1

    argument = "argument" if arg_c == 1 else "arguments"

    if arg_c == 0:
        print("0 arguments.")
    else:
        print("Number of {}: {}".format(argument, arg_c))

        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
