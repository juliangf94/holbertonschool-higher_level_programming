#!/usr/bin/python3
import hidden_4


def discovery():
    names = dir(hidden_4)
    for name in sorted(names):
        if name[:2] != "__":
            print("{}".format(name))


if __name__ == "__main__":
    discovery()
