#!/usr/bin/python3

import sys


with open(sys.argv[1], 'r') as input_string:
    string = input_string.readlines()  # is this broken in current version?


raw_string = (string[0])  # Not recognised for what they are
raw_motif = (string[1])


def find_motif(sequence, motif):
    positions = []
    slen = len(sequence)
    mlen = len(motif)
    for i in range(0, slen - mlen + 1):
        if sequence[i:i + mlen] == motif:
            positions.append(i + 1)
    return positions


list1 = find_motif(raw_string, raw_motif)

f = open('out.txt', 'w')  # Open the file

sys.stdout = f  # Serves at the write function?

str1 = ' '.join(str(i) for i in list1)

print(str1)  # Print this to file

f.close()  # Close the file
