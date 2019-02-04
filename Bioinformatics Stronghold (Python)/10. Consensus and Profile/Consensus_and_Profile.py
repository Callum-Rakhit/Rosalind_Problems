#!/usr/bin/python3

from Bio import SeqIO

import sys

with open(sys.argv[1], 'r') as input_string:
    string = input_string.readlines()  # Is this broken in current version?

raw_string = (string[0])  # Not recognised for what they are
raw_motif = (string[1])

# Import the fasta file using a biopython package

fasta_sequences = SeqIO.parse(open(sys.argv[1]), 'fasta')

with open(output_file) as out_file:
    for fasta in fasta_sequences:
        name, sequence = fasta.id, fasta.seq.tostring()
        new_sequence = some_function(sequence)
        write_fasta(out_file)

# The function to create a consensus sequence

def find_consensus(fasta_file):

    print(fasta_file)

    return


f = open('out.txt', 'w')  # Open the file

sys.stdout = f  # Serves at the write function?

str1 = ' '.join(str(i) for i in list1)

print(str1)  # Print this to file

f.close()  # Close the file