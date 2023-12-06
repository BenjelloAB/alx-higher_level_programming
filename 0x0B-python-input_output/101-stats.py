#!/usr/bin/python3
import sys


def print_status():
    '''
        function to print the status of the request...
    '''
    c = 0
    s = 0
    file_s = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for li in sys.stdin:
        line = li.split()
        try:
            s += int(line[-1])
            code = line[-2]
            status_codes[code] += 1
        except Exception:
            continue
        if c == 9:
            print("File s: {}".format(s))
            for key, val in sorted(status_codes.items()):
                if (val != 0):
                    print("{}: {}".format(key, val))
            c = 0
        c += 1
    if c < 9:
        print("File s: {}".format(s))
        for key, val in sorted(status_codes.items()):
            if (val != 0):
                print("{}: {}".format(key, val))


if __name__ == "__main__":
    print_status()
