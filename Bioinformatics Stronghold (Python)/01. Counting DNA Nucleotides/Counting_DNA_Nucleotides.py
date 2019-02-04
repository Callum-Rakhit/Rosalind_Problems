import sys

with open(sys.argv[1], 'r') as input_string:
    string = input_string.read()

print(string.count('A'))
print(string.count('C'))
print(string.count('G'))
print(string.count('T'))