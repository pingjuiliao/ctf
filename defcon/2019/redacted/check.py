#!/usr/bin/python

from pwn import *


alph = "+-=ABCDEFGHIJKLMNOPQRSTUVWXYZ {}"


def has_bit(bit) :
    arr = []
    for c in alph :
        if ord(c) & bit :
            arr.append(c)
    return arr
def not_has_bit(bit) :
    arr = []
    for c in alph :
        if not ord(c) & bit :
            arr.append(c)
    return arr
def is_num_bit(num) :
    arr = []
    for c in alph :
        cnt = 0
        for x in [1,2,4,8,16,32,64,128] :
            if ord(c) & x :
                cnt += 1
        if cnt == num :
            arr.append(c)
    return arr
def intersect(l1, l2) :
    return [v for v in l1 if v in l2]

if __name__ == "__main__" :
    has_bit(2)
    is_num_bit(6)
