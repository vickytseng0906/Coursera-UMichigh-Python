name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if line.startswith("From "):
        segment = line.split()
        counts[segment[1]] = counts.get(segment[1], 0) + 1
max_segment = None
max_count = 0
for address, count in counts.items():
    if count > max_count:
        max_count = count
        max_segment = address
print(max_segment, max_count)
