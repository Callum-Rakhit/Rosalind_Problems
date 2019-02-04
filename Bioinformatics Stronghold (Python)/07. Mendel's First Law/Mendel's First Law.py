#!/usr/bin/env python

import sys  # So you can take input from the command line
from scipy.misc import comb  # Usful for calculating probabilities

'''

A solution to the ROSALIND bioinformatics problem "Mendel's First Law"

Rosalind ID: IPRB

Rosalind Number: 007

URL: rosalind.info/problems/iprb/

'''

# Make a function to calculate the Mendelian probability


def mendel(homo_dom, hetro_dom, homo_rec):
    totalpossibilities = 4*comb(homo_dom + hetro_dom + homo_rec, 2)  # Total number of possible genotypes
    totalrecessive = 4*comb(homo_rec, 2) + 2*homo_rec*hetro_dom + comb(hetro_dom, 2)   # Number of recessive individuals
    return 1 - totalrecessive/totalpossibilities  # Likelihood of having the phenotype

# Get the answer and print it to a file


def answer():
    with open(sys.argv[1], 'r') as input_data:  # Read the input data
        k, m, n = map(int, input_data.read().strip().split())  # Assign the list to three variables, k, m and n

    prob = str(mendel(k, m, n))  # Calculaute the probability of expressing a phenotype given the input

    print(prob) # Print and save the answer

    with open('007_IRPB.txt', 'w') as output_data:  # Save the answer to file
        output_data.write(prob)

answer()  # Run the 'answer' function