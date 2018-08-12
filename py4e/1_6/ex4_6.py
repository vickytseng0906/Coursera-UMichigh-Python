hour = input("Hours")
rate = input("Rate per hour?")
h = float(hour)
r = float(rate)
diff = h - 40.0

def computepay(h,r):
    return diff * 1.5 * r + 40.0 * r

p = computepay(h,r)
print(p)
