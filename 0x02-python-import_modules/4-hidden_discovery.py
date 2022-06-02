

#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    
    all_stuff = dir(hidden_4)
    for i in range(1, len(all_stuff)):
        if all_stuff[i][0:2] != "__":
            print("{}".format(all_stuff[i]))
