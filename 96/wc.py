import string

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        read_data = f.read()
    lines = read_data.splitlines()
    words = read_data.split()
    chars = [char for char in list(read_data)]
    return ' '.join([str(len(lines)), str(len(words)), str(len(chars)), str(file_)])


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
