import sys


with open(sys.argv[1], 'r') as input_string:
    string = input_string.read()


def dna_to_rna(dna_string):
    rna_string = dna_string.replace('T', 'U')
    return rna_string


rna = dna_to_rna(string)
print(rna)