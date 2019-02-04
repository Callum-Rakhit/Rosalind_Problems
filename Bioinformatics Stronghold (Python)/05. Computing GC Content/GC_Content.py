import sys

# Load the fastq file

data = open(sys.argv[1], "r")
fastqFile = data.read()
data.close()

# Count the number os sequences

numberOfSequences = fastqFile.count('>')

#  Split into individual sequences and calculate GC content

list = []
list1 = []

sequence = fastqFile.split(">")[3]

for i in range(0, numberOfSequences):
    sequence = fastqFile.split(">")[i+1]
    postSequence = sequence.split("\n", 1)[1];
    postSequence = postSequence.strip()
    #print(postSequence)
    list.append(sequence.splitlines()[0])
    G = postSequence.count("G")
    C = postSequence.count("C")
    length = float(len(postSequence) - postSequence.count('\n') - postSequence.count(' '))
    GC = float(((G+C)/length)*100)
    #print(len(postSequence))
    GC = round(GC, 6)
    list1.append(GC)

max_value = max(list1)
max_index = list1.index(max_value)

print(list[max_index])
print(list1[max_index])
#print(fastqFile.split(">")[max_index+1])

# for i in numberOfSequences:
#     sequence[i] = numberOfSequences[i]



# "G" + "C" / len(sequence)

# Print largest value

