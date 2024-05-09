hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40:
    extra = (h - 40.0)
    over = (r * 1.5)
    overpay = (40 * r) + (extra * over)
    print(overpay)
else:
    print(h * r)
