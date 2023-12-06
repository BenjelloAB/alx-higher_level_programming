#!/usr/bin/python3


def print_stats(size, sc):
    """function that prints the status of the request

    Args:
        size (int): The read file size
        sc (dict): The count of status codes
    """
    print("File size: {}".format(size))
    for key in sorted(sc):
        print("{}: {}".format(key, sc[key]))


if __name__ == "__main__":
    import sys

    
    sc = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0
    size = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, sc)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in codes:
                    if sc.get(line[-2], -1) == -1:
                        sc[line[-2]] = 1
                    else:
                        sc[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, sc)

    except KeyboardInterrupt:
        print_stats(size, sc)
        raise
