#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    numargs = len(sys.argv)

    if numargs <= 1:
        print("0 arguments.")

    else:
        if numargs == 2:
            print("{:d} argument:".format(numargs - 1))

        else:
            print("{:d} arguments:".format(numargs - 1))

        for index in range(1, numargs):
            print("{:d}: {}".format(index, sys.argv[index]))
