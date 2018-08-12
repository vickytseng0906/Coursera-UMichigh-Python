fname = input("Enter file name: ") #prompt for file name
fh = open(fname) #open the file
lst = list() #build empty list
for line in fh:
    line = line.strip()
    line = line.split() # a list of words
    for word in line:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
