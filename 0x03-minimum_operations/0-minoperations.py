#!/usr/bin/python3
"""
calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    minOperations min operations
    Args:
        n :int
    """
    t = n
    i2 = 0
    i3 = 0
    i5 = 0
    i7 = 0
    i11 = 0
    if (n <= 0):
        return 0
    while (t % 2 == 0):
        i2 += 1
        t = t / 2
    while (t % 3 == 0):
        t = t / 3
        i3 += 1
    while (t % 5 == 0):
        t = t/5
        i5 += 1
    while (t % 7 == 0):
        t = t / 7
        i7 += 1
    while (t % 11 == 0):
        t = t / 11
        i11 += 1
    m = i5 * 5 + i3 * 3 + i2 * 2 + i7 * 7 + i11 * 11
    return m
