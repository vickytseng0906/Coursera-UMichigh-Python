name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    if line.startswith("From "):
        segment = line.split()
        time = segment[5]
        hour = time.split(":")
        count[hour[0]] = count.get(hour[0], 0) + 1

# can't sort a dictionary (just like map)
# so have to use a list

temp = list()
for k, v in count.items():
    temp.append((k, v))
temp.sort()

for hour, count in temp:
    print(hour, count)
