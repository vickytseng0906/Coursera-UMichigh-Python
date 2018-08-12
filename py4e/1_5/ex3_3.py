print ("ex3_2.py")
score = input ("Enter Score:") # bwteen 0.0 and 1.0
s = float(score)
try:
    if s >= 0.9:
        grade = str("A")
    elif s >= 0.8:
        grade = str("B")
    elif s >= 0.7:
        grade = str("C")
    elif s >= 0.6:
        grade = str("D")
    elif s < 0.6:
        grade = str("F")
except:
    print("Error. Please enter a score within 0.0 and 1.0")
    quit()
print (grade)
