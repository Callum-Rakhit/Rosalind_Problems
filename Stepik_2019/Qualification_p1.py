import sys

with open(sys.argv[1], 'r') as input_string:
    string = input_string.read()

T = int(string[0])
n1 = int(string[1][0])
a = int(string[1][1])
b = int(string[1][2])



def bees(T, n1, a, b):

    number = (a*n1) - (b*n1^2)

    if number

    return number


print bees(0, 1, new_size, old_size)


# Alex starts to grow a bee population. Since he cannot account for all the bees, he decides to count
# the amount of the bees in kilograms! Each day the population of bees evolves. Initially, on the first
# day, there were n1 kilograms of the bees. Suppose that at the i-th day the amount of bees is ni
# kilograms then on the next day the number of bees can be calculated by the following rule:
# ni+1=a⋅ni−b⋅n2i
#
# Alex now wonders what is the size of the population if he grows it indefinitely. Please, help him.
# Input format
#
# The first line of the input contains one integer T(1≤T≤50) - the number of test cases.
#
# Each of the next T lines contains a description of a test case. It consists of three real numbers with
# no more than three digits after the decimal point n1, a and b − the size of the initial generation and
# the trend constants (0≤n1≤10, 0≤a,b≤3)
#
# Output format
#
# The i-th line of the output should contain the limit (in the mathematical sense) of the population size in
# kilograms in the i-th test. If there is no limit output "−1".
#
# Your answer will be considered correct if its absolute or relative error doesn't exceed 10−4.
