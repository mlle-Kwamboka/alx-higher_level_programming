#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all_s = dir()
    for i in range(0, len(all_s)):
        if all_s[i][0:2] != "__":
            print("{}".format(all_s[i]))
