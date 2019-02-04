import sys


with open(sys.argv[1], 'r') as input_string:
    string = input_string.read()


def dna_complement(dna_string):
    dna_reverse = ''.join(reversed(dna_string))
    dna_reverse = dna_reverse.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c')
    dna_reverse = dna_reverse.upper()
    return dna_reverse


dna_reverse = dna_complement(string)
print(dna_reverse)