text = "X-DSPAM-Confidence:    0.8475";
subString = text.find("0")
last = text.find("5", subString)
target = text[subString:last+1]
print(float(target))
