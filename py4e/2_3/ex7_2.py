# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    index = line.find(":")
    newLine = line[index + 1:]
    count = count + 1
    total = total + float(newLine)
print("Average spam confidence:", float(total/count))
