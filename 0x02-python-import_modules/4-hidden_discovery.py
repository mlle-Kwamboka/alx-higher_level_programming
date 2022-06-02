

#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all_stuff = dir()
    for i in range(0, len(all_stuff)):
        if all_stuff[i][0:2] != "__":
            print("{}".format(all_stuff[i]))
