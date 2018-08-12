print ('ex_3.1')
hour = input('Hours?')
h = float(hour)
rate = input('Rate per hour?')
r = float(rate)
diff = h - 40
if h > 40.0:
    result = diff * 1.5 * r + 40.0 * r
else:
    result = h * r
print(result)
