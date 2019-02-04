import sys

file = open(sys.argv[1], "r")
sequences = file.read()
file.close()

string1 = sequences.splitlines()[0]
string2 = sequences.splitlines()[1]

result1 = ''
result2 = ''

maxLength = len(string2) if len(string1) <= len(string2) else len(string1)

for i in range(maxLength):
   base1 = string1[i:i+1]
   base2 = string2[i:i+1]
   if base1 != base2:
       result1 += base1
       result2 += base2

print(len(str(result1)))