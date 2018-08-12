import re

fname = input("Enter file name ")
if len(fname) < 1: fname = "regex_sum_115570.txt"

fhand = open(fname)
result = 0

for line in fhand:
    # return a list of integer
    x = re.findall('[0-9]+', line)
    for number in x:
        result += int(number)
print(result)
