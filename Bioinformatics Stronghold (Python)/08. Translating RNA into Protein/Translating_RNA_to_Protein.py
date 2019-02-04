#!/usr/bin/python3

import sys

codon_to_AA_letter = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                      "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                      "UAU": "Y", "UAC": "Y", "UAA": "\n", "UAG": "\n",  # Stop codons are newlines
                      "UGU": "C", "UGC": "C", "UGA": "\n", "UGG": "W",
                      "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                      "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                      "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                      "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                      "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                      "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                      "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                      "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                      "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                      "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                      "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                      "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}


def rna_to_protein(rnastr):
    chunks, chunk_size = len(rnastr), 3
    codons = [rnastr[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

    for i in codons:
            print(codon_to_AA_letter[i], end="")

    return


f = open('out.txt', 'w')  # Open the file

sys.stdout = f  # Serves at the write function?

rna_to_protein(sys.argv[1])  # Print this to file

f.close()  # Close the file
