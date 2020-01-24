#!/usr/bin/env python

import sys

def sxor(string, length) :
    r = 0
    for i in range(0, length) :
        r ^= ord(string[i])
    return r

if __name__ == "__main__" :
    if len(sys.argv) < 2 :
        print "Usage: %s <file_of_string>" % sys.argv[0]
        quit()

    with open(sys.argv[1], "rb") as f :
        s = f.read()
        f.close()

    print hex(sxor(s, 15))
    print hex(sxor(s[15:], 15))
