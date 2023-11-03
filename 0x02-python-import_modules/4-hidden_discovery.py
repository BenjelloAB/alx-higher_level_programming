#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    n = dir(hidden_4)
    for i in range(0, len(n)):
        if n[i][:2] != "__":
            print("{}".format(n[i]))
