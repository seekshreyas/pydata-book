#! /usr/bin/env python

"""
Ch02 Methods
-------------

Methods described in Ch02 in OpenData Book
"""

from collections import defaultdict

def get_counts(sequence):
    """
    Return counts of items in a list
    """

    counts = {}

    for item in sequence:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts



def get_counts2(sequence):
    counts = defaultdict(int)

    for item in sequence:
        counts[item] += 1

    return counts


def get_topcounts(count_dict, n=10):
    keypairs = [(count, tz) for tz, count in count_dict.items()]
    keypairs.sort()

    return keypairs[-n:]



def main():
    print __doc__

if __name__ == '__main__':
    main()
